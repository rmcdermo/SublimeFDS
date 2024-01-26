#!/usr/bin/env python3
# Randy McDermott
# Jan 2024
#
# This script reads FDS source files and parses the namelist groups for SublimeFDS syntax highlighting.

import re
import ruamel.yaml
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.explicit_start = True

# Set your fds repo location
fds_repo = "/Users/rmcdermo/GitHub/firemodels/fds"
text_file_1 = open(fds_repo+"/Source/read.f90","r")
text_file_2 = open(fds_repo+"/Source/geom.f90","r")
text_file_3 = open(fds_repo+"/Source/hvac.f90","r")
pattern = "namelist /"
delim = "|"

# initialize a dictionary to store the namelist parameters
nml_dict = dict()

for text_file in [text_file_1, text_file_2, text_file_3]:
    for line in text_file:
        line_lowercase = line.lower()
        if re.search(pattern, line_lowercase):
            split_line = line_lowercase.split("/",2)
            nml=split_line[1]

            next_line = split_line[2]
            clean_line = next_line.strip("\n& ")
            params=clean_line.split(",")

            while re.search("&", next_line):
                # read the next line
                next_line = next(text_file).lower()
                clean_line = next_line.strip("\n& ")
                next_line_params = clean_line.split(",")
                for nlp in next_line_params:
                    params.append(nlp)

            # remove empty stings from params list
            while "" in params:
                params.remove("")

            # print(nml)
            # print(params)

            nml_dict[nml] = str(delim.join(params)).upper()

    text_file.close()

# now edit the YAML file

with open('base.yaml') as stream:
   data = yaml.load(stream)

IDENT  = data['variables']['ident']
GROUPS = "("+str(delim.join(nml_dict.keys())).upper()+")"

# create tags from namelist groups
delim2 = "}}|{{"
TAGS = "{{"+str(delim2.join(nml_dict.keys()))+"}}"

new_variables = {'ident':IDENT,'groups':GROUPS}
for name in nml_dict.keys():
    new_variables.update({name:nml_dict[name]})
new_variables.update({'tags':TAGS})

data.update({'variables':new_variables})

data.yaml_set_comment_before_after_key('contexts', before="")

with open('FDS.sublime-syntax', 'wb') as stream:
   yaml.dump(data, stream)



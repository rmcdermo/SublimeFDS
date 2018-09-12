# SublimeFDS
[Sublime Text](https://www.sublimetext.com/) syntax highlighting for [FDS](https://pages.nist.gov/fds-smv/) input files

Here is an example using the "Monokai" Color Scheme:

![](test.png)

This syntax is based on the Sublime Fortran Namelist syntax.  The main differences are that namelist groups and parameters must be valid FDS inputs to be highlighted and there is better treatment of comments.

Pull requests welcome!

To install:

1. In sublime, go to Preferences -> Browse Packages. This will open the file explorer to the directory where packages are located. 

2. Clone the repo into this directory. 

3. Restart FDS. Go to Tools -> Command Window. Search for "Set Syntax: FDS" to activate the package. 
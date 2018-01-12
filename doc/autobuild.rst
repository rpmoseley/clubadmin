AutoBuild
=========

This file contains information regarding how to automate the process of building the Phoenix version of wxPython
without having to manually enter the commands. It attempts to detect which of the steps are required to generate
an upto date version of the code.

Detection of files present
--------------------------

This section outlines the specifics of the detection logic that removes a requirement to perform a particular part
of the overall build process.

Dox
---
In order to detect if the dox build command needs to be run, it is necessary to check if the directory
'ext/wxWidgets/docs/doxygen/out/xml' exists and contains files of the form '\*.xml', and is at least as old as the
repository directory 'ext/exWidgets'.

Etg
---
In order to detect if the etg build command needs to be run, it is necessary to check if the directory
'

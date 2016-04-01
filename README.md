# make-utility
basic GNU makefile scripts for building C++ projects

put makesetup folder in any appropriate location as you wish say: /home/userx/makesetup
usage:
/home/userx/makesetup/makesetup.py [path-to-new-c++-project]
ex:
/home/userx/makesetup/makesetup.py /home/userx/proj1

it sets up directories like below:
/home/userx/
  - /proj1/
    - /dumps    #location for .o,.lib,binaries
    - /scripts  #makefile util scripts
    - /src      #project code

in every folder under src,
copy makesetup/Makefile in to that folder and fill the empty vars

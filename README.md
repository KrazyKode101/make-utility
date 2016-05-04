# make-utility
basic GNU makefile scripts for building C++ projects

put makesetup folder in any appropriate location as you wish say: /home/userx/makesetup
usage:
/home/userx/makesetup/makesetup.py [path-to-new-c++-project]
ex:
/home/userx/makesetup/makesetup.py --setup /home/userx/proj1
/home/userx/makesetup/update/updateprojectroot.sh /home/userx/proj1

it sets up directories like below:
/home/userx/
  - /proj1/
    - /dumps    #location for .o,.lib,binaries
    - /scripts  #makefile util scripts
    - /src      #project code

in every folder under src,
copy makesetup/Makefile in to that folder and fill the below empty vars:
CPP_SOURCES =
SUBDIRS = 
LIB =
BIN =



important sources to learn about make utility:
http://opensourceforu.efytimes.com/2012/06/gnu-make-in-detail-for-beginners/
http://mrbook.org/blog/tutorials/make/

#!/usr/bin/python

import sys,os,commands,shutil

sw_loc = "/home/"+os.environ['USER']+"/makesetup/"
swscripts_loc = sw_loc+"scripts"

def setup_project(projectpath):
    os.makedirs(projectpath)
    os.makedirs(projectpath+'/scripts')
    os.makedirs(projectpath+'/dumps')
    os.makedirs(projectpath+'/src')

    shutil.copy(swscripts_loc+'/Makeutil',projectpath+'/scripts')
    shutil.copy(swscripts_loc+'/Makeconfig',projectpath+'/scripts')
    shutil.copy(swscripts_loc+'/Makefile',projectpath+'/scripts')

def main():
    args = sys.argv[1:]
    if len(args)==2:
        if args[0] == '--setup':
            setup_project(args[1])
    else:
        print "usage: makesetup.py --setup [project_path]"
        sys.exit(1)

if __name__ == "__main__":
	main()

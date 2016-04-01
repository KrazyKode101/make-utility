#!/usr/bin/python

import sys,os,commands,shutil

sw_loc = '/home/'+os.environ['USER']+'/makesetup/'
swscripts_loc = sw_loc+'scripts'

def setupproject(projectpath):
    os.makedirs(projectpath)
    os.makedirs(projectpath+'/scripts')
    os.makedirs(projectpath+'/dumps')
    os.makedirs(projectpath+'/src')

    shutil.copy(swscripts_loc+'/Makeutil',projectpath+'/scripts')
    shutil.copy(swscripts_loc+'/Makeconfig',projectpath+'/scripts')
    shutil.copy(swscripts_loc+'/Makefile',projectpath+'/scripts')

def main():
    args = sys.argv[1:]
    if not args or not len(args)==1:
        print "please enter a valid project path"
        print "usage: mainsetup.py /projectpath"
        sys.exit(1)

    setupproject(args[0])

if __name__ == "__main__":
	main()

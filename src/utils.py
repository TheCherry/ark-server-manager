import subprocess as sub
import os
import sys

def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def call(cmd, dir=None):
    print cmd
    if dir is None:
        dir = getScriptPath()
    p = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE, cwd=dir)
    output, errors = p.communicate()
    if(errors != ""):
        print errors
        #raise Exception(errors)
    return output

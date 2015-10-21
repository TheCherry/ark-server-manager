import subprocess as sub
import os
import sys
import pexpect
import pty
import errno
import select
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed, RotatingMarker
import re

global pbar, widgets, first


def getScriptPath():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def call_progressbar(data):
    f = re.search("progress: \d{0,3},\d{0,3} \((\d*) \/ (\d*)\)", data['child_result_list'][-1])
    if(f.group(1) != "0" and f.group(2) != "0"):
        if(not data["extra_args"][0]):
            data["extra_args"][2] = ProgressBar(widgets=data["extra_args"][1], maxval=int(f.group(2))).start()
            data["extra_args"][0] = True
        data["extra_args"][2].update(int(f.group(1)))


def call_steam_update(cmd, dir=None, progress_reg="Update state \(0x61\) downloading", progressbar=True):
    if dir is None:
        dir = getScriptPath()
    events = {}
    if(progressbar):
        events = {progress_reg: call_progressbar}

    ret = pexpect.run(dir + "/" + cmd,
                events=events,
                extra_args=[False,
                            ['Download Update: ', Percentage(), ' ', Bar(),
                             ' ', ETA(), ' ', FileTransferSpeed()],
                            None],
                withexitstatus=True)
    print(ret)
    return True


def call(cmd, dir=None):
    if dir is None:
        dir = getScriptPath()
    p = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE, cwd=dir)
    output, errors = p.communicate()
    if(errors != ""):
        print errors
        #raise Exception(errors)
    return output

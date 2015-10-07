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


def eventtest(t):
    f = re.search("progress: \d{0,3},\d{0,3} \((\d*) \/ (\d*)\)", t['child_result_list'][-1])
    #print("%s / %s" % (f.group(1), f.group(2)))
    if(f.group(1) != "0" and f.group(2) != "0"):
        if(not t["extra_args"][0]):
            t["extra_args"][2] = ProgressBar(widgets=t["extra_args"][1], maxval=int(f.group(2))).start()
            t["extra_args"][0] = True
        t["extra_args"][2].update(int(f.group(1)))


def call2(cmd, dir=None):
    if dir is None:
        dir = getScriptPath()
    pexpect.run(dir + "/" + cmd,
                events={'Update state \(0x61\) downloading': eventtest},
                extra_args=[False,
                            ['Download Update: ', Percentage(), ' ', Bar(),
                             ' ', ETA(), ' ', FileTransferSpeed()],
                            None])


def call3(cmd, dir=None):
    if dir is None:
        dir = getScriptPath()

    master_fd, slave_fd = pty.openpty()

    proc = sub.Popen(cmd,
                     shell=True, stdout=slave_fd, stderr=sub.STDOUT, close_fds=True, cwd=dir)
    timeout = .04 # seconds
    while 1:
        ready, _, _ = select.select([master_fd], [], [], timeout)
        if ready:
            data = os.read(master_fd, 512)
            if not data:
                break
            print(data)
        elif proc.poll() is not None: # select timeout
            assert not select.select([master_fd], [], [], 0)[0] # detect race condition
            break # proc exited
    os.close(slave_fd) # can't do it sooner: it leads to errno.EIO error
    os.close(master_fd)
    proc.wait()

    print("This is reached!")


def call(cmd, dir=None):
    if dir is None:
        dir = getScriptPath()
    p = sub.Popen(cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE, cwd=dir)
    output, errors = p.communicate()
    if(errors != ""):
        print errors
        #raise Exception(errors)
    return output

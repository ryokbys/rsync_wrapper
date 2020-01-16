#!/usr/bin/env python
"""
Wrap `rsync` command.

Usage:
  rsync_wrapper.py (up|down) [options]

Options:
  -h, --help  Show this message and exit.
  --dryrun    Not to operate, only output. [default: false]
"""
from __future__ import print_function

import os,sys
from docopt import docopt
import yaml
from subprocess import Popen, PIPE

__author__ = "RYO KOBAYASHI"
__version__ = "200116"

_conf_file = './.sync'
_conf_template = """
remote: 'host:path/to/dir/'
include: ['file1','file2','dir1']
exclude: ['file3','dir2']
option: ['-avzh',]
"""

_error_msg = """
Usage:
  rsync_wrapper.py (up|down) [options]

And there must be a config file of the name '.sync' in the current working directory.

The .sync file should be like the following:
""" + _conf_template

def read_conf(fname='./.rsync'):
    """
    Read the configuration file in the working directory
    to get the remote-path and files to be sent/receive.

    Input:
      fname: str
        Configuration file name.
    """
    if not os.path.exists(fname):
        raise IOError('File not exists: '+fname)
    with open(fname,'r') as f:
        conf = yaml.load(f)
    return conf


if __name__ == "__main__":

    args = docopt(__doc__)
    dry = args['--dryrun']
    up = args['up']
    down = args['down']

    if not os.path.exists(_conf_file):
        raise ValueError('No up config file '+_conf_file
                         +_error_msg)
    try:
        conf = read_conf(_conf_file)
    except:
        raise ValueError(_error_msg)

    cmd = ['rsync']
    local = './'
    if 'local' in conf.keys():
        local = conf['local']
    remote = conf['remote']
    # path = conf['path']
    option = conf['option']
    if dry:
        option.append('-n')
    cmd.extend(option)
    includes = conf['include']
    excludes = conf['exclude']
    for i in includes:
        cmd.append('--include="{0}"'.format(i))
    for e in excludes:
        cmd.append('--exclude="{0}"'.format(e))

    #...Opposite direction in up and down
    if up:
        cmd.append(local)
        cmd.append(remote)
    elif down:
        cmd.append(remote)
        cmd.append(local)
    
    #print(cmd)
    print(' '.join(cmd))
    #p = Popen(cmd,stdout=PIPE,stderr=PIPE)
    os.system(' '.join(cmd))
    # out,err = p.communicate()
    # print(out)
    #for line in iter(p.stdout.readline,''):
    #    print(line,end='')
    
    
    
    

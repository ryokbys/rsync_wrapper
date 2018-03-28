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

import os
from docopt import docopt
import yaml
from subprocess import Popen, PIPE

__author__ = "RYO KOBAYASHI"
__version__ = "180328"

_up_file = './.upsync'
_down_file = './.downsync'
_conf_template = """
src: './'
dst: 'host:path/to/dir/'
include: ['file1','file2','dir1'],
exclude: ['file3','dir2']
"""

_error_msg = """
Usage:
  rsync_wrapper.py (up|down) [options]

And there must be a config file of the name '.upsync' or '.downsync' (depending on up/down)
in the current working directory.

The .upsync and .downsync files should be like the following:
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

    if up:
        if not os.path.exists(_up_file):
            raise ValueError('No up config file '+_up_file
                             +_error_msg)
        conf = read_conf(_up_file)
    elif down:
        if not os.path.exists(_down_file):
            raise ValueError('No down config file '+_down_file
                             +_error_msg)
        conf = read_conf(_down_file)
    else:
        raise ValueError(_error_msg)

    cmd = ['rsync']
    src = conf['src']
    dst = conf['dst']
    # path = conf['path']
    option = '-avzh'
    if dry:
        option = '-avzhn'
    cmd.append(option)
    includes = conf['include']
    excludes = conf['exclude']
    for i in includes:
        cmd.append('--include={0}'.format(i))
    for e in excludes:
        cmd.append('--exclude={0}'.format(e))

    cmd.append(src)
    cmd.append(dst)

    #print(cmd)
    print(' '.join(cmd))
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)
    out,err = p.communicate()
    print(out)
    
    
    

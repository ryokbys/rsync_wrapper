#!/usr/bin/env python
"""
Wrap `rsync` command.

Usage:
  rsync_wrapper.py (up|down) [options]

Options:
  -h, --help  Show this message and exit.
  -d          Not to operate, only output. [default: false]
  -r, --remote REMOTE
              Remote host name. [default: None]
"""
from __future__ import print_function

import os
from docopt import docopt
import yaml
# from subprocess import Popen, PIPE

__author__ = "RYO KOBAYASHI"
__version__ = "200116"

_conf_file = './.sync'
_conf_template = """
remote_host: remote
remote_dir: 'path/to/dir/'
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
    dry = args['-d']
    remote_host = args['--remote']
    up = args['up']
    down = args['down']

    if not os.path.exists(_conf_file):
        raise ValueError('No up config file '+_conf_file
                         +_error_msg)
    try:
        conf = read_conf(_conf_file)
    except Exception as e:
        raise ValueError(_error_msg)

    cmd = ['rsync']
    
    if remote_host == 'None':  # Remote given by the option is used prior to that in conf-file.
        if 'remote_host' in conf.keys():
            remote_host = conf['remote_host']
        else:
            raise ValueError('Remote host must be specified in either option or conf-file.')

    cwd = os.getcwd()
    home = os.environ['HOME']+'/'
    remote_dir = cwd.replace(home,'')
    remote = remote_host +':' +remote_dir
    local = './'
    
    if 'option' in conf.keys():
        option = conf['option']
    else:  # default option
        option = ['-avzh']
    if dry:
        option.append('-n')
    cmd.extend(option)
    
    includes = []
    if 'include' in conf.keys():
        includes = conf['include']
    for i in includes:
        cmd.append('--include="{0}"'.format(i))
        
    excludes = []
    if 'exclude' in conf.keys():
        excludes = conf['exclude']
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
    
    
    
    

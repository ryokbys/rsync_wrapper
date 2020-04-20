# rsync_wrapper.py

## What is this?

This script helps syncing data of a certain directory in the local machine and the remote machine.
If you use this script, we strongly recommend that you make the directory structures of local and remote machines identical so that you do not need to specify the remote directory.

## Usage

```bash
$ rsync_wrapper.py down -r REMOTE
```
Then the files of the same path to the current working directory at the REMOTE host will be downloaded by using `rsync` command.

## Setup

1. Put `rsync_wrapper.py` script into any appropriate directory and make it executable.
2. cd to the directory where you want to use this script.
3. Run the script as
   ```
   $ rsync_wrapper.py up -r REMOTE
   ```
   Then the files specified in `.sync` will be uploaded using `rsync` command.

## Config file

If there is a `.sync` file with the following contents in the directory, the information will be used.
```
remote_host: remote
include: ['file1','file2','dir1']
exclude: ['file3','dir2']
option: ['-avzh']
```

- `remote_host` given by the option is used prior to that in config-file.
- The current working directory in the local machine is also used for the remote directory, except when `remote_dir: path/to/dir/` is specified in the config-file.


## Make aliases to the workflows

Write the lines into your `.bashrc` or `.bash_profile` file.
```
alias upsync='rsync_wrapper.py up'
alias downsync='rsync_wrapper.py down'
```
Then you can run the script by `upsync` or `downsync`.

## Contact

Please contact me if you have questions or requests.
ryo.kbys [at] gmail.com


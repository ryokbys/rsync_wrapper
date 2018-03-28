# rsync_wrapper.py

## Setup

1. Put `rsync_wrapper.py` script into any appropriate directory and make it executable.
2. cd to the directory that you want to use this rsync_wrapper.py.
3. Make `.upsync` or `.downsync` file of the following contents in the directory.
   ```
   src: './'
   dst: 'host:path/to/dir/'
   include: ['file1','file2','dir1']
   exclude: ['file3','dir2']
   option: ['-avzh']
   ```
4. Modify the `.uprsync` or `.downsync` file.
5. Run the script as
   ```
   $ rsync_wrapper.py up
   ```
   Then the files specified in `.upsync` will be uploaded using `rsync` command.

## Make nicknames

Write the lines into your `.bashrc` or `.bash_profile` file.
```
alias upsync='rsync_wrapper.py up'
alias downsync='rsync_wrapper.py down'
```
Then you can run the script by `upsync` or `downsync`.


## Contact

Please contact me if you have questions or requests.
ryo.kbys [at] gmail.com


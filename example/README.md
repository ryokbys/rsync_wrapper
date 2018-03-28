# Example

In this example, there are files in the `src/` directory.
```bash
$ tree src/
src/
|-- dir1
|   `-- file1
`-- dir2
    |-- dir2-1
    |   |-- dir2-1-1
    |   |   `-- file1
    |   `-- file1
    `-- file2
```

And there is `.upsync` file as following.
```
src: 'src/'
dst: 'dst/'
include: ['dir1/','file1']
exclude: ['*']
option: ['-avzh']
```

```bash
$ rsync_wrapper.py up
```
This command will create `src/dir1/` directory in the `dst/` directory, and copy `src/dir1/file1` file into `dst/dir1/`.


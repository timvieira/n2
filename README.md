n2: A command-line tool for searching and indexing notes
========================================================

Install
-------

Install the scripts via pip.

```bash
$ pip install -e .
```

Add config file to your home directory.

```bash
$ cp example-notesrc ~/.notesrc
```

Edit `~/.notesrc`. Be sure to specify a valid path for here `n2` can store its
indexes.

```
[config]
index = ~/projects/notes/.index
```

Now, run the following command to build in the search index.

```
$ n2 --build
```

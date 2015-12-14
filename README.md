gener8
======

Summary
-------

Simple yet powerful universal scaffolding tool.

Caution
-------

**This software is still in experimental stages.** Please report any bug you might encounter.

Description
-----------

Use this program to create all kind of configurable project templates and deploy them easily.

Synopsis
--------

```
usage: gener8 [-h] [-l] [-d DEST] [templates [templates ...]]

The script will successively copy content from "templates" folders to the
destination folder called "DEST". You can choose from where templates are found
by setting the "GENER8_DIR" environment variable to a valid path.

positional arguments:
  templates

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list available templates and exit
  -d DEST, --dest DEST  destination directory path
```

Prerequisites
-------------

- python

Dependencies
------------

- PyYAML `pip install pyyaml`
- EmPy `pip install empy`

Installation
------------

### From PyPI

`pip install gener8`

OR

### From sources

```
git clone https://github.com/lelongg/gener8.git
cd gener8
python setup.py install
```

Quick start
-----------

[This repository](https://github.com/lelongg/gener8_templates.git) provide some templates you can use to create new projects.

Clone it to the default gener8 templates repository location.
`git clone https://github.com/lelongg/gener8_templates.git ~/.gener8`

Check if **gener8** is aware of our new templates directory.
`gener8 -l` should display some templates like *python_module* as available templates.

For generating a new repository based on this particular template:
`gener8 python_module`

This should ask several questions:
`Please provide a destination [python_module-2015-12-14]:` press *enter*
`Do you want to use default values (y/n) [y] ?` press *n* then *enter*

For each variable displayed you can provide a value then hit *enter* or directly press
enter to use default value given between square brackets.

`Do you want to save values (y/n) [n] ?` press *n* then enter

You should now have a directory called *python_module-2015-12-14* (the actual date might change...) located in your current directory
and it's content should be customized with the input values you provided.


What is a template ?
--------------------

A template is a folder tree located in your template directory.

Your default template directory is _~/.gener8_.

You can change it by setting the **GENER8_DIR** environment variable to a valid path.

A template can provide two special files at is root: *config.gener8* and *default.gener8*.

Both of them must respect [YAML syntax](http://www.yaml.org/spec/1.2/spec.html).


### config.gener8

Here is a sample *config.gener8*:

```
parents: [template1, template2]

parse: [README.md, src/**/*.c, doc/**/*]

pre:
    - python: |
        print('do this')
        print('do that')

post:
    - bash: |
        echo "do this"
        echo "do that"
    - ruby: |
        puts 'do this'
        puts 'do that'
```

It must be a YAML dictionnary containing the following keys:

*Note:* each key is optional

- __parents__
: A YAML list containing parent templates name.
Parent templates will be applied to the destination before applying the current one.

- __parse__
: The list of files which will be parsed.
Files and directories globbing is supported.

- __pre__
: List of commands to be run before template copy.

- __post__
: List of commands to be run after template copy.

*pre* and *post* are lists of key/value pairs where each key is an executable shell and each value is a string.
For every pair, the shell corresponding to the key will be run and fed with the content of the value.


### default.gener8

Here is a sample *default.gener8*:

```
title: The Bride of the Witches

date: 2002-06-25

author:
    firstname: Rowland Kilback
    lastname: KILBACK
    address: 3417 Dave Rue Apt. 285\nLake Blakeshire, KS 15200-1215
    email: rkilback@gmail.com
```

It must be a YAML dictionnary but the content can be anything.


### Name expansion

File and folder names in template tree will be expanded according to [EmPy syntax](http://www.alcyone.com/pyos/empy)
which allow python processing.

Data from *default.gener8* are easily accessible.

For example, given the previous *default.gener8*, a file named `@author.firstname` will be renamed `Rowland`.

Some more examples :

```
    @(date).py                      ->  2002-06-25.py
    @author.lastname.lower()        ->  kilback
    @(title.replace(' ', '_')).md   ->  The_Bride_of_the_Witches.md
```


### File parsing

File selected from the *parse* key in the *config.gener8* file will be parsed according to [EmPy syntax](http://www.alcyone.com/pyos/empy).

Data from *default.gener8* are accessible the same way as for name expansion.


Sequence of operation
---------------------

- Commands from *pre* key in the *config.gener8* file will be run.

- the whole template tree (excepting *config.gener8* and *default.gener8* if provided) will be copied to the destination folder which will be created if it doesn't exist.

- Every file and folder name from the template tree will be expanded according to [EmPy syntax](http://www.alcyone.com/pyos/empy).

- Every file selected from the *parse* key in the *config.gener8* file will be parsed according to [EmPy syntax](http://www.alcyone.com/pyos/empy).

- Commands from *post* key in the *config.gener8* file will be run.


Data overriding
---------------

Data from *default.gener8* file can be overrided by user.

You just have to provide a file called *data.gener8* in the folder from where you run the **gener8** command.

This file should reproduce the *default.gener8* structure from the template you want to deploy.

You are free to change any of the values and your modifications will override default values.

If you run the **gener8** command to deploy a template which contains a *default.gener8* file
from a directory which does not contain a *data.gener8* file, it will ask you if you want to
manually override default parameters or use default ones.

Whatever you answer, you will be asked to save these values (manually provided or default ones) to
a *data.gener8* file in the current folder.


How to create a template ?
--------------------------

### Steps to follow:

1. Create a folder into **gener8** template dir.

That's it ! You've created your first **gener8** template !

*Note:* You might wonder where the **gener8** template dir is located: type `gener8 -h` and the answer will be given.
Change it easily by setting **GENER8_DIR** environment variable. For example: `export GENER8_DIR="/my/new/template/repository"`.
You might want to set it permanently by adding this change to your *.bashrc*. For example: `echo export GENER8_DIR="/my/new/template/repository" >> ~/.bashrc`.

### Next (optional) steps are:

- Add files and folders you want to be part of your template inside the directory you've just created.
- Use name and content expansion syntax to make your template customizable.
- Add the variables you want to be available for expansion and their default values into a *default.gener8* file located in the main folder of your template.
- Add a *config.gener8* file in the main folder of your template
- Add a *parse* list to your *config.gener8* file in which you can add file names that should be processed for expansion.
- Add a *parent* list to your *config.gener8* file.
- Add commands to be executed in the *pre* and *post* section of your *config.gener8* file.

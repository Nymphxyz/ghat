=======
GHat
=======

Overview
========

GHat (Github Hat Decorator/Green Hat Decorator) is a quick hack for decorating your GitHub contribution calendar with a specific date file.

You can create any patterns you want on the Contribution Calendar.

If you mess up everything, just delete the corresponding repository and your contribution calendar will be restored.

It uses the GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environmental variables to make commits appear in the past.

**Be warned that GHat will clobber your repository's commit history. Therefore it's better for you to use it on a new repository.**

GHat contains a main.py file and a web with JS.
The process is to customize the pattern you want through the Web page, and the Web will generate a date.txt which contains the date of the commit and the number of times it should be committed. Then main.py will read the file, make commits based on the date and number of times in the file and finally push it to your repository.

Check the GHat homepage at https://github.com/Nymphxyz/ghat for more information.

Requirements
============
* Git
* Python 3.6+
* Works on Linux, Windows, macOS(hasn't been tested)

Install
=======

The quick way:

    pip install ghat

Usage
=====

Before you use it remember to check your git email address.
It must be same with your email in github, otherwise all commits won't appear in the contribution calendar.

    git config --global user.email  "your@email.address"

First cd to your repository directory.

Then you have 3 choices:

The simplest way is type "ghat" and follow the instructions:

    ghat


Or use shortcut to initialize a new repository and make commit (This  will **create** two files ``README.md`` and ``work.txt``):

    ghat -i your_repository_url /path/to/date.file


Or use shortcut to make commits on an existing repository (This operation will **create** and **overwrite** file ``work.txt``):

    ghat /path/to/date.file


Documentation
=============

Check details at https://github.com/Nymphxyz/ghat

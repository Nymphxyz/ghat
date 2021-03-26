#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @author: XYZ
# @file: setup.py
# @time: 2021.03.11
# @desc:

from setuptools import setup, find_packages

def readme_file():
    with open("README.rst") as f:
        return f.read()

setup(name="ghat",
      version="0.1.3",
      description="A quick hack for decorating your GitHub contribution calendar through a specific date file.",
      long_description=readme_file(),
      license="MIT",
      packages=find_packages(exclude=["demo", "img"]),
      author="Nymphxyz",
      author_email="xyz.hack666@gmail.com",
      url="https://github.com/Nymphxyz/ghat",
      entry_points={
        "console_scripts": [
            "ghat=ghat.__main__:main",
        ]
      },
      include_package_data=True,
    )


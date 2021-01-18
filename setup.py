#!/usr/bin/env python

from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='Homework1',
      version='1.0',
      description='Python Distribution Utilities',
      author='Hatimalhazmi',
      packages=find_packages('src'),
      package_dir={'':'/home/travis/build/Hatimalhazmi/Homework1/tests/test_dictionaries.py''src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )

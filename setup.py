#!/usr/bin/env python

from distutils.core import setup
#from setuptools import setup, find_packages

setup(name='timegrok',
      version='0.2',
      description='Python Module for interpreting human time expressions.',
      author='Robert Seward',
      author_email='rseward@bluestone-consulting.com',
      url='http://www.bluestone-consulting.com/',
      # python package dirs will require at a minimum an empty __init__.py file
      #   in them.

      packages=['timegrok' ],
      scripts=[],      

      package_dir={'timegrok':'src/timegrok'}
    )

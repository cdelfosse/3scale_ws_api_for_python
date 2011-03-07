# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='ThreeScalePY',
      version='1.0',
      py_modules=['ThreeScalePY'],
      install_requires=[
          "libxml2"
      ],
)


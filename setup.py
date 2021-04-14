"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='doc_manager-api',
    version='0.1.0',
    description='doc_manager-api',
    long_description=README,
    author='Oscar Valenzuela',
    author_email='oscar.valen115@gmail.com',
    url='https://github.com/oscar-valen115/doc_manager-api',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)

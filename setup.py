#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='scim',
    version='0.2.0',
    description='A python interface to produce and consume System for'
                ' Cross-domain Identity Management (SCIM) messages.',
    author='Concordus Applications',
    author_email='support@concordusapps.com',
    url='http://github.com/concordusapps/python-scim',
    package_dir={'scim': 'src/scim'},
    packages=find_packages('src'),
    install_requires=(
        # Extensions to the standard Python datetime module.
        # Provides ability to easily parse ISO 8601 formatted dates.
        'python-dateutil'
    ),
)

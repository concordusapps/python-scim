#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pkgutil import get_importer
from os import path

# Calculate the base directory of the project.
BASE_DIR = path.abspath(path.dirname(__file__))

# Navigate, import, and retrieve the version of the project.
VERSION = get_importer(path.join(BASE_DIR, 'src')).find_module(
    'scim').load_module().__version__

setup(
    name='scim',
    version=VERSION,
    description='A python interface to produce and consume System for'
                ' Cross-domain Identity Management (SCIM) messages.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3'
    ],
    author='Concordus Applications',
    author_email='support@concordusapps.com',
    url='http://github.com/concordusapps/python-scim',
    package_dir={'scim': 'src/scim'},
    packages=find_packages(path.join(BASE_DIR, 'src')),
    install_requires=(
        # Extensions to the standard Python datetime module.
        # Provides ability to easily parse ISO 8601 formatted dates.
        'python-dateutil'
    ),
    extras_require={
        'test': (
            # Test runner.
            'pytest',

            # Ensure PEP8 conformance.
            'pytest-pep8',

            # Ensure test coverage.
            'pytest-cov',
        )
    }
)

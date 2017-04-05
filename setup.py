#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='flake8_formatter_abspath',
    version='0.1.0',
    description="A flake8 formatter plugin that shows the absolute path of files with warnings",
    long_description=readme + '\n\n' + history,
    author="Josh Smeaton",
    author_email='josh.smeaton@gmail.com',
    url='https://github.com/jarshwah/flake8_formatter_abspath',
    packages=[
        'flake8_formatter_abspath',
    ],
    package_dir={'flake8_formatter_abspath':
                 'flake8_formatter_abspath'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flake8_formatter_abspath',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

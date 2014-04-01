#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='sci-crawler',
    version='0.0.1',
    author='ZOwl',
    author_email='zhhbug@gmail.com',
    license='LICENSE.txt',
    description='sci-crawler',
    test_suite='tests',
    packages=find_packages(exclude=['tests']),
    install_requires=[
       "scrapy",
    ]
)

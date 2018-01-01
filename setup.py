#!/usr/bin/env python3

from setuptools import setup, find_packages


DESCRIPTION = open("README.rst").read()

setup(
    name="cowdict",
    version="0.2",
    url="https://www.github.com/csernazs/cowdict",
    packages=find_packages(),
    author="Zsolt Cserna",
    author_email="zsolt.cserna@gmail.com",
    description="Copy-on-write dictionary",
    long_description=DESCRIPTION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

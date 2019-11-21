#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="it-stacky",
    version="0.0.1",
    packages=find_packages(),
    tests_require=["mock" "requests"],
    test_suite="tests",
    extras_require={"dev": ["tox",]},
)

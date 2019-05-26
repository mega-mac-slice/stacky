#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='stacky',
    version='0.0.5',
    packages=find_packages(),
    url='https://gitlab.com/mega-mac-slice/stacky',
    license='MIT',
    author='mega-mac-slice',
    author_email='megamacslice@protonmail.com',
    description='A service management tool for local development.',
    entry_points={
        'console_scripts': [
            'stacky = stacky.app:main'
        ]
    },
    data_files=[
        'README.md',
        'requirements.txt'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').readlines(),
    tests_require=[
        'mock'
    ],
    test_suite='tests',
    extras_require={
        'dev': [
            'pycodestyle',
            'tox',
            'bumpversion',
            'mock'
        ]
    }
)

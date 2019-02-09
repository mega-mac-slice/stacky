from setuptools import setup, find_packages
from stacky import __version__

setup(
    name='stacky',
    version=__version__,
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
    install_requires=open('requirements.txt').readlines(),
    tests_require=[
        'mock'
    ],
    test_suite='tests',
    extras_require={
        'dev': [
            'pycodestyle',
            'tox'
        ]
    }
)

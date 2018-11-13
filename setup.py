from setuptools import setup, find_packages
from stacky import __version__

setup(
    name='stacky',
    version=__version__,
    packages=find_packages(),
    url='',
    license='',
    author='mega-mac-slice',
    author_email='megamacslice@protonmail.com',
    description='Micro-Service management for local development.',
    entry_points={
        'console_scripts': [
            'stacky = stacky.app:main'
        ]
    },
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').readlines()
)

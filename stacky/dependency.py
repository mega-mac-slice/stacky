import os

from stacky import commands

GIT = 'git'
HTTP = 'http'
DIR = 'dir'


def parse(dependency):
    if dependency.startswith('git@'):
        name, _ = os.path.splitext(os.path.basename(dependency))
        return GIT, name

    if dependency.startswith('http'):
        name, _ = os.path.splitext(os.path.basename(dependency))
        return HTTP, name

    if os.path.exists(dependency):
        name, _ = os.path.splitext(os.path.basename(dependency))
        return DIR, name


def retrieve(dependency):
    kind, name = parse(dependency)
    path = os.path.join(os.getcwd(), name)
    if os.path.exists(path):
        return path

    if kind == GIT:
        commands.git_clone(dependency)

    return path

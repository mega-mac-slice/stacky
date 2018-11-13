import os

from stacky import dependency
from stacky import config


class StackyAccumulator:
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir
        self.stacky_files = []


def iterate(stacky_acc, stacky_file):
    os.chdir(stacky_acc.parent_dir)

    for item in stacky_file.dependencies:
        path = dependency.retrieve(item)
        if config.exists(path):
            stacky_file_child = config.read(path)
            stacky_acc.stacky_files.append(stacky_file_child)
            iterate(stacky_acc, stacky_file_child)


def accumulate(parent_dir, stacky_file):
    stacky_acc = StackyAccumulator(parent_dir)
    iterate(stacky_acc, stacky_file)
    return stacky_acc.stacky_files

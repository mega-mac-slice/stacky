import os
from typing import List

from stacky import dependency
from stacky import config


class StackyAccumulator:
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir
        self.stacky_files = []


def iterate(stacky_acc: 'StackyAccumulator', stacky_file: 'config.StackyFile', extra: List[str] = None):
    os.chdir(stacky_acc.parent_dir)

    for item in stacky_file.stack:
        path = dependency.retrieve(item)
        if config.exists(path):
            stacky_file_child = config.read(path)
            stacky_acc.stacky_files.append(stacky_file_child)
            iterate(stacky_acc, stacky_file_child)

    if extra:
        for key in extra:
            if key not in stacky_file.extra:
                raise ValueError(f'extra: {key} does not exist in: {stacky_file.file_path}')

            for item in stacky_file.extra[key]:
                path = dependency.retrieve(item)
                if config.exists(path):
                    stacky_file_child = config.read(path)
                    stacky_acc.stacky_files.append(stacky_file_child)
                    iterate(stacky_acc, stacky_file_child)


def accumulate(parent_dir: str, stacky_file: 'config.StackyFile', extra: List[str] = None) -> List['config.StackyFile']:
    stacky_acc = StackyAccumulator(parent_dir)
    iterate(stacky_acc, stacky_file, extra)
    return stacky_acc.stacky_files

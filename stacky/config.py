import os
import sys
import json
import collections
import logging

logger = logging.getLogger()


class StackyFile:
    def __init__(self):
        self.dir_path = ''
        self.file_path = ''

        self.name = ''
        self.commands = {
            'start': None,
            'stop': None,
            'status': None
        }

        self.stack = []
        self.extra = {}


def exists(path: str) -> bool:
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')
    return os.path.exists(path)


def read(path: str) -> 'StackyFile':
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')

    if not exists(path):
        logging.error(f'.stacky.json file: {path} not found.\n')
        sys.exit(-1)

    config = StackyFile()
    with open(path) as f:
        obj = json.load(f)

    config.dir_path = os.path.dirname(path)
    config.file_path = path

    name = obj.get('name')
    if name:
        config.name = name

    commands = obj.get('commands')
    if commands:
        config.commands = {
            'start': commands.get('start'),
            'stop': commands.get('stop'),
            'status': commands.get('status'),
        }

    stack = obj.get('stack')
    if stack:
        for dependency in stack:
            config.stack.append(dependency)

    extra = obj.get('extra')
    if extra:
        for key, value in extra.items():
            config.extra[key] = value

    return config


def write(obj: 'StackyFile', path: str):
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')

    with open(path, 'w') as f:
        json.dump(collections.OrderedDict({
            'name': obj.name,
            'commands': obj.commands,
            'stack': obj.stack,
            'extra': obj.extra
        }), f, indent=4)

import os
import sys
import json


class StackyFile:
    def __init__(self):
        self.dir_path = ''
        self.file_path = ''

        # serde to .stack.json
        self.name = ''
        self.commands = {
            'start': None,
            'stop': None,
            'status': None
        }

        self.dependencies = []


def exists(path):
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')
    return os.path.exists(path)


def read(path):
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')

    if not exists(path):
        sys.stderr.write('.stacky.json file: {0} not found.\n'.format(path))
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
            config.dependencies.append(dependency)

    return config


def write(obj, path):
    if not path.endswith('.stacky.json'):
        path = os.path.join(path, '.stacky.json')

    with open(path, 'w') as f:
        json.dump({
            'name': obj.name,
            'commands': obj.commands,
            'stack': obj.dependencies
        }, f)

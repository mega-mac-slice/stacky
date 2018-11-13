import os
import sys
import argparse
import collections

from stacky import config
from stacky import iter
from stacky import commands


def init_command(args):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, '.stacky.json')

    name = os.path.basename(current_dir)

    stacky_file = config.StackyFile()
    stacky_file.name = name
    stacky_file.commands = {
        'start': 'make start',
        'stop': 'make stop',
        'status': 'make status'
    }
    config.write(stacky_file, file_path)
    print(file_path)


def start_command(args):
    current_dir, parent_dir = os.getcwd(), os.path.abspath('..')

    stacky_file_parent = config.read(current_dir)
    stacky_file_children = iter.accumulate(parent_dir, stacky_file_parent)

    seen = set()
    # Reverse children so we start dependencies from deepest part of tree.
    for child in stacky_file_children[::-1]:
        if child.name in seen:
            continue

        os.chdir(child.file_dir)
        # If its already running no need to start it.
        if commands.check_status_ok(child):
            seen.add(child.name)
            continue

        if commands.start(child):
            # Block until dependency is running.
            commands.poll_check_status_ok(child)
            seen.add(child.name)


def stop_command(args):
    current_dir, parent_dir = os.getcwd(), os.path.abspath('..')

    stacky_file_parent = config.read(current_dir)
    stacky_file_children = iter.accumulate(parent_dir, stacky_file_parent)

    seen = set()
    # Reverse children so we start dependencies from deepest part of tree.
    for child in stacky_file_children[::-1]:
        if child.name in seen:
            continue

        os.chdir(child.file_dir)
        if commands.check_status_ok(child) and commands.stop(child):
            seen.add(child.name)


def status_command(args):
    current_dir, parent_dir = os.getcwd(), os.path.abspath('..')

    stacky_file_parent = config.read(current_dir)
    stacky_file_children = iter.accumulate(parent_dir, stacky_file_parent)

    lookup = collections.OrderedDict()
    for stacky_file in [stacky_file_parent] + stacky_file_children:
        if stacky_file.name in lookup:
            continue

        os.chdir(stacky_file.dir_path)
        lookup[stacky_file.name] = commands.status(stacky_file)

    for name, status in lookup.iteritems():
        print('{0} - {1}'.format(name, status))


def paths_command(args):
    current_dir, parent_dir = os.getcwd(), os.path.abspath('..')

    stacky_file_parent = config.read(current_dir)
    stacky_file_children = iter.accumulate(parent_dir, stacky_file_parent)

    unique = set([i.file_dir for i in stacky_file_children])

    for file_dir in unique:
        sys.stdout.write(file_dir)


def main():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()

    parser = subparsers.add_parser('init', help='create default .stacky.json')
    parser.set_defaults(func=init_command)

    parser = subparsers.add_parser('start', help='start stack services')
    parser.set_defaults(func=start_command)

    parser = subparsers.add_parser('stop', help='stop stack services')
    parser.set_defaults(func=stop_command)

    parser = subparsers.add_parser('status', help='status of stack services')
    parser.set_defaults(func=status_command)

    parser = subparsers.add_parser('paths', help='list local directory paths of dependencies')
    parser.set_defaults(func=paths_command)

    args = main_parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

import sys
import subprocess
import time
import logging

logger = logging.getLogger()


def _call_command(command):
    code = subprocess.call(command, shell=True)
    return code == 0, code


def _check_output_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return True, 0, output
    except subprocess.CalledProcessError as ex:
        return False, ex.returncode, None


def start(stacky_file):
    if not stacky_file.commands or 'start' not in stacky_file.commands:
        return False

    command = stacky_file.commands.get('start')
    success, code = _call_command(command)

    if not success:
        logger.error('command[start]: {0} failed with code: {1}.'.format(command, code))

    return True


def stop(stacky_file):
    if not stacky_file.commands or 'stop' not in stacky_file.commands:
        return False

    command = stacky_file.commands.get('stop')
    success, code = _call_command(command)

    if not success:
        logging.error('command[stop]: {0} failed with code: {1}.'.format(command, code))

    return True


def status(stacky_file):
    if not stacky_file.commands or 'status' not in stacky_file.commands:
        return None

    command = stacky_file.commands.get('status')
    if command is None:
        return None

    success, code, output = _check_output_command(command)

    return output


def check_status_ok(stacky_file):
    return status(stacky_file) == 'ok'


def poll_check_status_ok(stacky_file, timeout=30):

    attempts = 0
    while attempts < timeout:
        if check_status_ok(stacky_file):
            return True

        attempts += 1
        time.sleep(1)

    return False


def git_clone(dependency):
    assert dependency.startswith('git@')
    command = 'git clone {0}'.format(dependency)
    success, code = _call_command(command)

    if not success:
        logging.error('git[clone]: {0} failed with code: {1}.'.format(command, code))

import subprocess
import time
import logging
import typing

from stacky.config import StackyFile

logger = logging.getLogger()


def _call_command(command) -> (bool, int):
    code = subprocess.call(command, shell=True)
    return code == 0, code


def _check_output_command(command) -> (bool, int, str):
    try:
        output = subprocess.check_output(command, shell=True)
        return True, 0, output
    except subprocess.CalledProcessError as ex:
        return False, ex.returncode, None


def start(stacky_file) -> bool:
    if not stacky_file.commands or not stacky_file.commands.get('start'):
        return False

    command = stacky_file.commands.get('start')
    success, code = _call_command(command)

    if not success:
        logger.error('command[start]: {0} failed with code: {1}.'.format(command, code))

    return True


def stop(stacky_file) -> bool:
    if not stacky_file.commands or not stacky_file.commands.get('stop'):
        return False

    command = stacky_file.commands.get('stop')
    success, code = _call_command(command)

    if not success:
        logging.error('command[stop]: {0} failed with code: {1}.'.format(command, code))

    return True


def status(stacky_file: 'StackyFile') -> typing.Optional[bytes]:
    if not stacky_file.commands or not stacky_file.commands.get('status'):
        return None

    command = stacky_file.commands.get('status')
    if command is None:
        return None

    success, code, output = _check_output_command(command)

    return output


def run(stacky_file, command_name) -> typing.Optional[bool]:
    if not stacky_file.commands or not stacky_file.commands.get(command_name):
        return None

    command = stacky_file.commands.get(command_name)
    success, code = _call_command(command)

    if not success:
        logger.error('command[run]: {0} failed with code: {1}.'.format(command, code))
        return False

    return True


def check_status_ok(stacky_file: 'StackyFile') -> bool:
    return b'ok' in status(stacky_file)


def poll_check_status_ok(stacky_file: 'StackyFile', timeout=30) -> bool:

    attempts = 0
    while attempts < timeout:
        logger.debug(f'polling status | {stacky_file.name}\t {attempts}/{timeout}')
        if check_status_ok(stacky_file):
            return True

        attempts += 1
        time.sleep(1)

    return False


def git_clone(dependency: str):
    assert dependency.startswith('git@')
    command = 'git clone {0}'.format(dependency)
    success, code = _call_command(command)

    if not success:
        logger.error('git[clone]: {0} failed with code: {1}.'.format(command, code))

import subprocess
import time
import logging
import typing

from stacky.config import StackyFile

logger = logging.getLogger()


def _call_command(command: str) -> (bool, int):
    code = subprocess.call(command, shell=True)
    return code == 0, code


def _check_output_command(command: str) -> (bool, int, bytes):
    try:
        output = subprocess.check_output(command, shell=True)
        return True, 0, output
    except subprocess.CalledProcessError as ex:
        return False, ex.returncode, None


def start(stacky_file: StackyFile) -> bool:
    if not stacky_file.commands or not stacky_file.commands.get("start"):
        return False

    command = stacky_file.commands.get("start")
    success, code = _call_command(command)

    if not success:
        logger.error(f"command[start]: {command} failed with code: {code}.")

    return True


def stop(stacky_file: StackyFile) -> bool:
    if not stacky_file.commands or not stacky_file.commands.get("stop"):
        return False

    command = stacky_file.commands.get("stop")
    success, code = _call_command(command)

    if not success:
        logging.error(f"command[stop]: {command} failed with code: {code}.")

    return True


def status(stacky_file: StackyFile) -> typing.Optional[bytes]:
    if not stacky_file.commands or not stacky_file.commands.get("status"):
        return None

    command = stacky_file.commands.get("status")
    if command is None:
        return None

    success, code, output = _check_output_command(command)

    return output


def run(stacky_file: StackyFile, command_name: str) -> typing.Optional[bool]:
    if not stacky_file.commands or not stacky_file.commands.get(command_name):
        return None

    command = stacky_file.commands.get(command_name)
    success, code = _call_command(command)

    if not success:
        logger.error(f"command[run]: {command} failed with code: {code}.")
        return False

    return True


def check_status_ok(stacky_file: StackyFile) -> bool:
    return b"ok" in status(stacky_file)


def poll_check_status_ok(stacky_file: StackyFile, timeout=30) -> bool:
    attempts = 0
    while attempts < timeout:
        logger.debug(f"polling status | {stacky_file.name}\t {attempts}/{timeout}")
        if check_status_ok(stacky_file):
            return True

        attempts += 1
        time.sleep(1)

    return False


def git_clone(dependency: str):
    is_ssh = dependency.startswith("git@")
    is_http = dependency.startswith("http") and dependency.endswith(".git")

    if not (is_ssh or is_http):
        raise ValueError(f"git[clone]: only supports ssh or http and not {dependency}.")

    command = f"git clone {dependency}"
    success, code = _call_command(command)

    if not success:
        logger.error(f"git[clone]: {command} failed with code: {code}.")

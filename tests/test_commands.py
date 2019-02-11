from unittest import TestCase
import mock
from contextlib import contextmanager

from stacky import commands
from stacky import config


class TestStartCommand(TestCase):
    @contextmanager
    def context(self, command_result):
        with mock.patch('stacky.commands._call_command', return_value=command_result) as call_command:
            self.call_command = call_command
            yield

    def test_success(self):
        with self.context((True, 0)):
            stack_file = config.StackyFile()
            stack_file.commands['start'] = 'make start'
            result = commands.start(stack_file)
            self.assertTrue(result)
            self.call_command.assert_called_with('make start')

    def test_not_defined_success(self):
        with self.context((True, 0)):
            stack_file = config.StackyFile()
            commands.start(stack_file)
            result = commands.start(stack_file)
            self.assertFalse(result)
            self.assertFalse(self.call_command.called)

    def test_error(self):
        with self.context((False, 1)):
            stack_file = config.StackyFile()
            stack_file.commands['start'] = 'make start'
            result = commands.start(stack_file)
            self.assertTrue(result)
            self.call_command.assert_called_with('make start')


class TestStatusCommand(TestCase):
    @contextmanager
    def context(self, command_result):
        with mock.patch('stacky.commands._check_output_command', return_value=command_result) as check_output_command:
            self.check_output_command = check_output_command
            yield

    def test_success(self):
        with self.context((True, 0, b'ok')):
            stack_file = config.StackyFile()
            stack_file.commands['status'] = 'make status'
            result = commands.status(stack_file)
            self.assertEqual(b'ok', result)
            self.check_output_command.assert_called_with('make status')

    def test_not_defined_success(self):
        with self.context((True, 0, b'ok')):
            stack_file = config.StackyFile()
            commands.status(stack_file)
            result = commands.status(stack_file)
            self.assertIsNone(result)
            self.assertFalse(self.check_output_command.called)

    def test_error(self):
        with self.context((False, 1, b'fail')):
            stack_file = config.StackyFile()
            stack_file.commands['status'] = 'make status'
            result = commands.status(stack_file)
            self.assertEqual(b'fail', result)
            self.check_output_command.assert_called_with('make status')


class TestRunCommand(TestCase):
    @contextmanager
    def context(self, command_result):
        with mock.patch('stacky.commands._call_command', return_value=command_result) as call_command:
            self.call_command = call_command
            yield

    def test_success(self):
        with self.context((True, 0)):
            stack_file = config.StackyFile()
            stack_file.commands['reset'] = 'make reset'
            result = commands.run(stack_file, 'reset')
            self.assertTrue(result)
            self.call_command.assert_called_with('make reset')

    def test_not_defined_success(self):
        with self.context((True, 0)):
            stack_file = config.StackyFile()
            commands.status(stack_file)
            result = commands.run(stack_file, 'reset')
            self.assertIsNone(result)
            self.assertFalse(self.call_command.called)

    def test_error(self):
        with self.context((False, 1)):
            stack_file = config.StackyFile()
            stack_file.commands['reset'] = 'make reset'
            result = commands.run(stack_file, 'reset')
            self.assertFalse(result)
            self.call_command.assert_called_with('make reset')

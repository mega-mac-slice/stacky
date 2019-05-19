import mock

from argparse import Namespace
from unittest import TestCase
from contextlib import contextmanager

from stacky import app
from stacky import config


class TestInitCommand(TestCase):
    def test_success(self):
        with mock.patch('stacky.app.config.write') as write:
            app.init_command(None)
            self.assertTrue(write.called)


class TestStartCommand(TestCase):
    @contextmanager
    def context(self, stack_file: 'config.StackyFile'):
        with mock.patch('stacky.app.config.read', return_value=stack_file) as read, \
                mock.patch('stacky.app.commands.check_status_ok') as check_status_ok, \
                mock.patch('stacky.app.commands.start') as start:
            self.read = read
            self.check_status_ok = check_status_ok
            self.start = start
            yield

    def test_empty_stack_success(self):
        stacky_file = config.StackyFile()
        with self.context(stacky_file):
            app.start_command(Namespace(extra=None))

            self.assertTrue(self.read.called)
            self.assertFalse(self.check_status_ok.called)
            self.assertFalse(self.start.called)

from unittest import TestCase
import mock

from stacky import app


class TestApp(TestCase):
    def test_init_command_success(self):
        with mock.patch('stacky.app.config.write') as write:
            app.init_command(None)
            self.assertTrue(write.called)

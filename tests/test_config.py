from unittest import TestCase

from stacky import config


class TestStackyFile(TestCase):
    def test_stacky_file_default_success(self):
        result = config.StackyFile()
        self.assertIsNotNone(result)

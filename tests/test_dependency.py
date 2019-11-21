from unittest import TestCase

from stacky import dependency


class TestParse(TestCase):
    def test_http_git(self):
        result = dependency.parse("https://gitlab.com/mega-mac-slice/dev-postgres.git")
        self.assertEqual((dependency.GIT, "dev-postgres"), result)

    def test_ssh_git(self):
        result = dependency.parse("git@gitlab.com:mega-mac-slice/dev-postgres.git")
        self.assertEqual((dependency.GIT, "dev-postgres"), result)

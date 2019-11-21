from unittest import TestCase

import os
import shutil
import subprocess

root = os.path.dirname(__file__)
target = os.path.join(root, "extra")


class TestExtraStackOnly(TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(target)
        subprocess.call("stacky start", shell=True)

    def test_retrieved_success(self):
        os.chdir(root)
        self.assertTrue(os.path.exists(os.path.join(root, "dev-postgres")))

    def test_status_success(self):
        os.chdir(target)
        result = subprocess.check_output(
            "stacky status", shell=True, stderr=subprocess.STDOUT
        )
        self.assertEqual(1, result.count(b"ok"), result)

    @classmethod
    def tearDownClass(cls):
        os.chdir(root)
        shutil.rmtree(os.path.join(root, "dev-postgres"), ignore_errors=True)


class TestExtraStackAndOneExtra(TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(target)
        subprocess.call("stacky start redis", shell=True)

    def test_retrieved_success(self):
        os.chdir(root)
        self.assertTrue(os.path.exists(os.path.join(root, "dev-postgres")))
        self.assertTrue(os.path.exists(os.path.join(root, "dev-redis")))

    def test_status_success(self):
        os.chdir(target)
        result = subprocess.check_output(
            "stacky status redis", shell=True, stderr=subprocess.STDOUT
        )
        self.assertEqual(2, result.count(b"ok"), result)

    @classmethod
    def tearDownClass(cls):
        os.chdir(root)
        shutil.rmtree(os.path.join(root, "dev-postgres"), ignore_errors=True)
        shutil.rmtree(os.path.join(root, "dev-redis"), ignore_errors=True)


class TestExtraStackAndMultiExtra(TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(target)
        subprocess.call("stacky start redis elasticsearch", shell=True)

    def test_retrieved_success(self):
        os.chdir(root)
        self.assertTrue(os.path.exists(os.path.join(root, "dev-postgres")))
        self.assertTrue(os.path.exists(os.path.join(root, "dev-redis")))
        self.assertTrue(os.path.exists(os.path.join(root, "dev-elasticsearch")))

    def test_status_success(self):
        os.chdir(target)
        result = subprocess.check_output(
            "stacky status redis elasticsearch", shell=True, stderr=subprocess.STDOUT
        )
        self.assertEqual(3, result.count(b"ok"), result)

    @classmethod
    def tearDownClass(cls):
        os.chdir(root)
        shutil.rmtree(os.path.join(root, "dev-postgres"), ignore_errors=True)
        shutil.rmtree(os.path.join(root, "dev-redis"), ignore_errors=True)
        shutil.rmtree(os.path.join(root, "dev-elasticsearch"), ignore_errors=True)

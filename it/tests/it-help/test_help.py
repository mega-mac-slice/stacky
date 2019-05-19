from unittest import TestCase

import subprocess


class TestHelp(TestCase):
    def test_help(self):
        result = subprocess.check_output('stacky', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))

    def test_start_help(self):
        result = subprocess.check_output('stacky start --help', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))
        
    def test_status_help(self):
        result = subprocess.check_output('stacky status --help', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))
    
    def test_stop_help(self):
        result = subprocess.check_output('stacky stop --help', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))
    
    def test_run_help(self):
        result = subprocess.check_output('stacky run --help', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))
    
    def test_paths_help(self):
        result = subprocess.check_output('stacky paths --help', shell=True, stderr=subprocess.STDOUT)
        self.assertTrue(result.startswith(b'usage:'))
    
    


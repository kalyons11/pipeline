import os
import unittest

from .. import app


class TestClass(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.tester = app.test_client()

    def test_env(self):
        self.assertEqual(os.getenv('FOO'), 'BAR')

#unittest

import unittest

from password_checker import p

class TestCommon(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pwd = p

    def test_A(self):
        self.assertEqual(self.pwd, p)

    def test_B(self):
        self.assertEqual(self.pwd, p)

#unittest

import unittest

from simple_piglatin_converter import translate

def translate(string):
	return string

class translateTest(unittest.TestCase):
	def test(self):
		self.assertEqual(type(translate("will")), str)
		self.assertEqual(type(translate("dog")), str)
		self.assertEqual(type(translate("category")), str)
		self.assertEqual(type(translate("chatter")), str)
		self.assertEqual(type(translate("trash")), str)
		self.assertEqual(type(translate("andela")), str)
		self.assertEqual(type(translate("electrician")), str)

if __name__ == '__main__':
	unittest.main()
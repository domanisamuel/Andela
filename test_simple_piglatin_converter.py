import unittest

from simple_piglatin_converter import translate
# PIG LATIN
# Translate the provided string to pig latin.
# Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an "ay".
# If a word begins with a vowel you just add "way" to the end.

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

# TESTING
# translate("california") should return "aliforniacay".
# translate("paragraphs") should return "aragraphspay".
# translate("glove") should return "oveglay".
# translate("algorithm") should return "algorithmway".
# translate("eight") should return "eightway".
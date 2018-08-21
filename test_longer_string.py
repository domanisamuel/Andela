#unittest

import unittest

from longer_string import andela

class TestAssertEqual(unittest.TestCase):
    def setUp(self):
        super(TestAssertEqual, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def testString(self):
        s1 = 'zzz\nzzz'
        s2 = 'zzz\nzzz'
        self.assertEqual(s1,s2)

    def testUnicode(self):
        s1 = u'zzz\nzzz'
        s2 = u'zzz\nzzz'
        self.assertEqual(s1,s2)

if __name__ == '__main__':
    unittest.main()


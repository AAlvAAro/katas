# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
import unittest
from two_to_one import longest

class TwoToOneTest(unittest.TestCase):

    def test_longest(self):
        cases = [
            { 'str1': 'xyaabbbccccdefww', 'str2': 'xxxxyyyyabklmopq', 'longest': 'abcdefklmopqwxy'},
            { 'str1': 'abcdefghijklmnopqrstuvwxyz', 'str2': 'abcdefghijklmnopqrstuvwxyz',
              'longest': 'abcdefghijklmnopqrstuvwxyz'}
        ]

        for case in cases:
            self.assertEqual(case['longest'], longest(case['str1'], case['str2']))
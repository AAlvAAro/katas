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
            { 's1': 'xyaabbbccccdefww', 's2': 'xxxxyyyyabklmopq', 'longest': 'abcdefklmopqwxy'},
            { 's1': 'abcdefghijklmnopqrstuvwxyz', 's2': 'abcdefghijklmnopqrstuvwxyz',
              'longest': 'abcdefghijklmnopqrstuvwxyz'}
        ]

        for case in cases:
            self.assertEqual(case['longest'], longest(case['s1'], case['s2']))
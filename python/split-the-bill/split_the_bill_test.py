import unittest
from split_the_bill import split_the_bill

class SplitTheBillTest(unittest.TestCase):

    def test_split_the_bill(self):
        cases = [
            {
                'group': { 'A': 20, 'B': 15, 'C': 10 },
                'split': { 'A': 5, 'B': 0, 'C': -5 }
            },
            {
                'group': { 'Alvaro': 100, 'Bere': 250, 'Ramon': 50 },
                'split': { 'Alvaro': -33, 'Bere': 117, 'Ramon':  -83 }
            }
        ]

        for case in cases:
            self.assertEqual(case['split'], split_the_bill(case['group']))


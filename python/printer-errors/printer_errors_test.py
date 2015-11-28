import unittest
from printer_errors import printer_errors

class PrinterErrorsTest(unittest.TestCase):

    def test_printer_errors(self):
        cases = [
            {'ratio': '8/22', 'str': 'aaaxbbbbyyhwawiwjjjwwm'},
            {'ratio': '0/14', 'str': 'aaabbbbhaijjjm'}
        ]

        for case in cases:
            self.assertEqual(case['ratio'], printer_errors(case['str']))
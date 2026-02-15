"""
test_02_package_discount_part_2.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the package_discount_part_2 function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch
from io import StringIO
import sys, os

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from srcmain import package_discount_part_2

class TestPackageDiscountPart2(unittest.TestCase):
    """Test package_discount_part_2() by mocking input() and capturing printed output."""

    # case_01: qty 5 (no discount)
    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_01_no_discount(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('0.00', output)
        self.assertIn('0.00', output)
        self.assertIn('495.00', output)

    # case_02: qty 15 (20% discount)
    @patch('builtins.input', side_effect=['15'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_02_discount_20(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('20.00', output)
        self.assertIn('297.00', output)
        self.assertIn('1188.00', output)

    # case_03: qty 25 (30% discount)    
    @patch('builtins.input', side_effect=['25'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_03_discount_30(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('30.00', output)
        self.assertIn('742.50', output)
        self.assertIn('1732.50', output)

    # case_04: qty 55 (40% discount)
    @patch('builtins.input', side_effect=['55'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_04_discount_40(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('40.00', output)
        self.assertIn('2178.00', output)
        self.assertIn('3267.00', output)

    # case_05: qty 120 (50% discount)
    @patch('builtins.input', side_effect=['120'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_05_discount_50(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('50.00', output)
        self.assertIn('5940.00', output)
        self.assertIn('5940.00', output)

    # case_06: qty negative (should print error)
    @patch('builtins.input', side_effect=['-10'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_06_negative_qty(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('Quantity must be numeric and positive', output,
                      msg="Should print an error for negative quantity. Your function should print 'Quantity must be numeric and positive.'")

    # case_07: qty not numeric (should print error)
    @patch('builtins.input', side_effect=['abc'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_07_non_numeric_qty(self, mock_stdout, mock_input):
        package_discount_part_2()
        output = mock_stdout.getvalue()
        self.assertIn('Quantity must be numeric and positive', output,
                      msg="Should print an error for non-numeric quantity. Your function should print 'Quantity must be numeric and positive.'")

if __name__ == '__main__': # run this if its being run directly ie the main or else dont run this

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPackageDiscountPart2)
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("Test passed")   # Goes to stdout (for autograder)
    else:   
        print("Test failed")
        sys.exit(1)            # Non-zero exit code signals failure
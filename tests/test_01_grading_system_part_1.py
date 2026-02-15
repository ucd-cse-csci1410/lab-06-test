"""
test_01_grading_system_part_1.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the grading_system_part_1 function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

#inbuilt modules of assertion can be taken advantage of.
import unittest


from unittest.mock import patch 

from io import StringIO

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.main import grading_system_part_1  

class TestGradingSystemPart1(unittest.TestCase):
    """Test grading_system_part_1() by mocking input() and capturing printed output."""


   
    # case_01: letter grade A for average >= 90
    @patch('builtins.input', side_effect=['95', '92', '98'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_01_grading_system_part_1_letter_grade_A(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('95.000', output,
                      msg="Output should contain average 95.000 for scores 95, 92, 98. Check if the average has 3 decimal places")
        self.assertIn('A', output,
                      msg="Letter grade should be A when average is 95.000. Check if the letter grade is in uppercase.")
    
    # case_02: letter grade B for average >= 80
    @patch('builtins.input', side_effect=['85', '82', '88'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_02_grading_system_part_1_letter_grade_B(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('85.000', output,
                      msg="Output should contain average 85.000 for scores 85, 82, 88. Check if the average has 3 decimal places")
        self.assertIn('B', output,
                      msg="Letter grade should be B when average is 85.000. Check if the letter grade is in uppercase.")
    

    # case_03: letter grade C for average >= 70
    @patch('builtins.input', side_effect=['75', '72', '78'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_03_grading_system_part_1_letter_grade_C(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('75.000', output,
                      msg="Output should contain average 75.000 for scores 75, 72, 78. Check if the average has 3 decimal places")
        self.assertIn('C', output,
                      msg="Letter grade should be C when average is 75.000. Check if the letter grade is in uppercase.")

    # case_04: letter grade D for average >= 60
    @patch('builtins.input', side_effect=['65', '62', '68'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_04_grading_system_part_1_letter_grade_D(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('65.000', output,   
                      msg="Output should contain average 65.000 for scores 65, 62, 68. Check if the average has 3 decimal places")
        self.assertIn('D', output,
                      msg="Letter grade should be D when average is 65.000. Check if the letter grade is in uppercase.")
    
    # case_05: letter grade F for average < 60
    @patch('builtins.input', side_effect=['55', '52', '58'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_05_grading_system_part_1_letter_grade_F(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('55.000', output,
                      msg="Output should contain average 55.000 for scores 55, 52, 58. Check if the average has 3 decimal places")
        self.assertIn('F', output,
                      msg="Letter grade should be F when average is 55.000. Check if the letter grade is in uppercase.")
    
    # case_06: error message for non-numeric test scores
    @patch('builtins.input', side_effect=['abc', '100', '70'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_06_grading_system_part_1_non_numeric_test_scores(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('Test score must be numeric and positive', output,
                      msg="Your function should print 'Test score must be numeric and positive' when the test score is non-numeric.")
    
    # case_07: error message for negative test scores
    @patch('builtins.input', side_effect=['-10', '100', '70'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_07_grading_system_part_1_negative_test_scores(self, mock_stdout, mock_input):
        grading_system_part_1()

        output = mock_stdout.getvalue()
        self.assertIn('Test score must be numeric and positive', output,
                      msg="Your function should print 'Test score must be numeric and positive' when the test score is negative.")
    

    # case_08: test scores out of range (110, 110, 110) → average > 100 → Undefined
    @patch('builtins.input', side_effect=['110', '110', '110'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_08_grading_system_part_1_average_out_of_range(self, mock_stdout, mock_input):
        grading_system_part_1()
        output = mock_stdout.getvalue()
        self.assertIn('Average test score is out of range', output,
                      msg="Average for scores 110, 110, 110 should be out of range. Your function should print 'Average test score is out of range'")
        self.assertIn('Undefined', output,
                      msg="Letter grade for scores 110, 110, 110 should be  Undefined.Your function should print 'Undefined'")
    
   
if __name__ == '__main__': # run this if its being run directly ie the main or else dont run this

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGradingSystemPart1)
    runner = unittest.TextTestRunner(stream=sys.stderr) 
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("Test passed")   # Goes to stdout (for autograder)
    else:
        print("Test failed")
        sys.exit(1)            # Non-zero exit code signals failure
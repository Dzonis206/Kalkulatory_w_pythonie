import unittest
import math

# Import the functions to test from main.py
# If main.py is not in the same directory, adjust the import accordingly
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import evaluate_expression, advanced_operation

class TestCalculator(unittest.TestCase):
    def test_basic_addition(self):
        self.assertEqual(evaluate_expression("2+2"), 4)

    def test_basic_subtraction(self):
        self.assertEqual(evaluate_expression("5-3"), 2)

    def test_basic_multiplication(self):
        self.assertEqual(evaluate_expression("3*4"), 12)

    def test_basic_division(self):
        self.assertEqual(evaluate_expression("10/2"), 5)

    def test_invalid_expression(self):
        self.assertEqual(evaluate_expression("2/0"), "Error")
        self.assertEqual(evaluate_expression("abc"), "Error")

    def test_square(self):
        self.assertEqual(advanced_operation("3", "x²"), "9.0")

    def test_square_root(self):
        self.assertEqual(advanced_operation("16", "√x"), "4.0")

    def test_reciprocal(self):
        self.assertEqual(advanced_operation("4", "1/x"), "0.25")

    def test_advanced_invalid(self):
        self.assertEqual(advanced_operation("0", "1/x"), "Error")
        self.assertEqual(advanced_operation("abc", "x²"), "Error")
        self.assertEqual(advanced_operation("9", "unknown"), "Error")

if __name__ == "__main__":
    unittest.main()
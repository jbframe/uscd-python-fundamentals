#!/usr/bin/env python
# Assignment 3
# Question 3
# Given the following code below saved as a file named calc.py, import the file into a new file named test_calc.py and write a unittest to test each function:

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x-y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     if y==0:
#         raise ValueError('Cannot divide by zero!')
#     return x / y;

# *Note: To test out the exception you will need to run the context manager:
# with self.assertRaises(ValueError):
#  calc.divide(1, 0)
# ** Use the following EvenNum.py  downloadand EvenNum_test.py  downloads a guide.
# In your unittest you may want to try various options such as using two positive numbers, a positive and negative number and two negative numbers for each test.

import calc
import unittest

class TestCalc(unittest.TestCase):
  def test_add(self):
    self.assertEqual(calc.add(1,2), 3)
    self.assertEqual(calc.add(-1,2), 1)
    self.assertEqual(calc.add(-1,-2), -3)

  def test_subtract(self):
    self.assertEqual(calc.subtract(1,2), -1)
    self.assertEqual(calc.subtract(-1,2), -3)
    self.assertEqual(calc.subtract(-1,-2), 1)

  def test_multiply(self):
    self.assertEqual(calc.multiply(1,2), 2)
    self.assertEqual(calc.multiply(-1,2), -2)
    self.assertEqual(calc.multiply(-1,-2), 2)

  def test_divide(self):
    self.assertEqual(calc.divide(1,2), 0.5)
    self.assertEqual(calc.divide(-1,2), -0.5)
    self.assertEqual(calc.divide(-1,-2), 0.5)
    with self.assertRaises(ValueError):
      calc.divide(1, 0)

if __name__ == '__main__':
  unittest.main()
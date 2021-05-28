#!/usr/bin/env python
# Assignment 3
# Question 1
# Write a Python class which has two methods get_String and print_String. The function get_String accepts and returns a string passed into a constructor. The function print_String prints the string in upper case. The class should have a constructor that returns the string entered by the user as an argument. Create an object to test execute the functions from the class.

class Strings:
  def __init__(self, userString):
    self.userString = userString
  def get_String(self):
    return self.userString
  def print_String(self):
    return print(self.userString.upper())

instanceOfStringsClass = Strings("hi")
print(instanceOfStringsClass.get_String()) # expected result 'hi'
instanceOfStringsClass.print_String() # expected result 'HI'
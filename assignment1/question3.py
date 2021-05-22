#!/usr/bin/env python
# Assignment 1
# Question 3
# Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

def reverseLongString():
  reverseString = ""
  while True:
    longString = input("Please enter a long string containing multiple words: ")
    longList = longString.split(" ")
    try:
      if len(longList) < 2:
        raise Exception
    except Exception:
      print("Your string must be two or more words!")
    else:
      for i in reversed(longList):
        reverseString += i + " "
      return print(reverseString)
reverseLongString()
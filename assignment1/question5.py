#!/usr/bin/env python
# Assignment 1
# Question 5
# Exercise Question 3: Given 2 strings, s1, and s2, return a new string made of the first, middle and last char each input string
# Given:

# s1 = "America"
# s2 = "Japan"
# Expected Output:
# AJrpan

def twoStringFirstMiddleLastChar(str1, str2):
  result = ''
  result += str1[0]
  result += str2[0]
  def middleCharHelper(str):
    if len(str) % 2 == 1:
      middleChar = int((len(str) - 1) / 2)
      return str[middleChar]
    else:
      firstMiddleChar = int(len(str) / 2)
      return str[firstMiddleChar - 1] + str[firstMiddleChar]
  result += middleCharHelper(str1)
  result += middleCharHelper(str2)
  result += str1[len(str1) - 1]
  result += str2[len(str2) - 1]
  return result

# Test Cases
s1 = "America"
s2 = "Japan"
s3 = "Mexico"
s4 = "Canada"
print(twoStringFirstMiddleLastChar(s1, s2)) # AJrpan
print(twoStringFirstMiddleLastChar(s3, s4)) # MCxinaoa
#!/usr/bin/env python
# Assignment 1
# Question 4
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.

def firstAndLastElements(numbersList):
  if len(numbersList) >= 2:
    results = list()
    results.append(numbersList[0])
    results.append(numbersList[len(numbersList) - 1])
    return results

# Test Cases
a = [5, 10, 15, 20, 25]
b = [5, 25]
c = [5]
print(firstAndLastElements(a)) # [5, 25]
print(firstAndLastElements(b)) # [5, 25]
print(firstAndLastElements(c)) # None
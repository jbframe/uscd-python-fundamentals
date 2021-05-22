#!/usr/bin/env python
# Assignment 1
# Question 2
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

def commonElementsFromTwoLists(a, b):
  results = list()
  for i in a:
    for j in b:
      if i == j and i not in results:
        results.append(i)
  return print(results)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [1, 1, 2, 4, 5]
d = [1, 2, 3]

commonElementsFromTwoLists(a, b) # [1, 2, 3, 5, 8, 13]
commonElementsFromTwoLists(c, d) # [1, 2]
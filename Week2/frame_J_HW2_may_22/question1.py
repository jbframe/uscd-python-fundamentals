#!/usr/bin/env python
# Assignment 2
# Question 1
# Given a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evenElementsList = [i for i in a if i%2==0]

# test
print(evenElementsList) # [4, 16, 36, 64, 100]
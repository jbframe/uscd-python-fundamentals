#!/usr/bin/env python
# Assignment 3
# Question 4
# Write a Python program that counts how many lines and how many words there are in a file. Use the file attached here  download > About_Python-1.txt.
def countLinesAndWords(fileName):
  fHandle = open('About_Python-1.txt')

  count = 0
  for line in fHandle:
      count += 1
  print(count)
fileName = 'About_Python-1.txt'
countLinesAndWords(fileName)
#!/usr/bin/env python
# Assignment 3
# Question 4
# Write a Python program that counts how many lines and how many words there are in a file. Use the file attached here  download > About_Python-1.txt.
def countLinesAndWords(fileName):
  fHandle = open(fileName)
  lineCount = 0
  wordCount = 0
  for line in fHandle:
    lineCount += 1
    wordCount += len(line.rstrip().split(' '))
  fHandle.close()
  print("The file " + str(fileName) + " has " + str(lineCount) + " lines and " + str(wordCount) + " words.")

# Tests
fileName = 'About_Python-1.txt'
countLinesAndWords(fileName) # Expected result "The file About_Python-1.txt has 7 lines and 102 words."
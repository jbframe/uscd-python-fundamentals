#!/usr/bin/env python
# Assignment 3
# Question 4
# Write a Python program that reads in the file from the problem above and writes the document completely backward to a new text file (the last letter of the entire document becomes the first and so on so the document can be read from bottom to top and from right to left)
def writeDocumentBackwardToFile(fileName):
  fHandle = open(fileName)
  resultLineList = []
  result = ""
  newFHandle = open("DocumentBackward.txt", "w")
  for line in fHandle:
    #Assuming that we want to strip excess spaces and keep the same line breaks.
    stripedLine = line.rstrip()
    resultLineList.append(stripedLine[::-1])
  resultLineList.reverse()
  for i in range(len(resultLineList)):
    result += resultLineList[i]
    if i != len(resultLineList) - 1:
      result += '\n'
  newFHandle.write(result)
  fHandle.close()
  newFHandle.close()
# Tests
fileName = 'About_Python-1.txt'
writeDocumentBackwardToFile(fileName) # Expected result: A new file called DocumentBackward.txt with backwards txt is created
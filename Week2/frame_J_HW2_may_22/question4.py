#!/usr/bin/env python
# Assignment 2
# Question 4
# Fibonacci Sequence is the series of positive numbers that is created by add the previous two numbers to create the next number in a sequence. For example, A Fibonacci sequence starts with the number 1. Then next number adds the two that number plus the previous number which happens to be 0+1 so the sequence would now be 0+1 = 1 giving us the sequence 1, 1, The next number is created by add these two 1+1 = 2 giving us 1,1,2 and so on until we have 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...
# Write a recursive function that asks the user how many Fibonacci numbers to generate and then generates them.

def HowManyFibonacci():
    # input with error handeling
  inputComplete = False
  nTerms = int
  while inputComplete == False:
    try:
      nTerms = int(input("Please enter the desired number of fibonacci numbers to display: "))
      if isinstance(nTerms, int) is False or nTerms < 1:
        raise Exception
    except Exception:
      print("Please be sure to make your input as a positive integer number!")
    else:
      inputComplete = True
  # recursive function
  def Fibonacci(n):
    # base case
    if n <= 1:
      return n
    # recursive case
    else:
      return (Fibonacci(n-1) + Fibonacci(n-2))
  # calculate nTerms
  result = ''
  for i in range(nTerms):
    result += (str(Fibonacci(i)) + ', ')
  return print(result[:-2])
HowManyFibonacci()
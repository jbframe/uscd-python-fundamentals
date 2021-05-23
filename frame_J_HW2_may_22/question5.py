#!/usr/bin/env python
# Assignment 2
# Question 5
# Write a function or set of functions that asks a user for a number and determine whether the number is prime or not. Recall that a prime number is a number that has no divisors.

def isPrime():
    # input with error handeling
  inputComplete = False
  num = int
  while inputComplete == False:
    try:
      num = int(input("Please enter a number to check if it is prime: "))
      if isinstance(num, int) is False or num < 1:
        raise Exception
    except Exception:
      print("Please be sure to make your input as a positive integer number!")
    else:
      inputComplete = True
  # recursive function
  def checkForPrime(n, div = None):
    # base case
    if div is None:
        div = n - 1
    while div >= 2:
      if n % div == 0:
        return print("Your number is not prime.")
      else:
        return checkForPrime(n, div - 1)
    else:
      return print("Your number is prime.")
  checkForPrime(num)
isPrime()
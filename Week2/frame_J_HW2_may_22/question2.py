#!/usr/bin/env python
# Assignment 2
# Question 2
# Write a program that creates a random number from 0 to 100 and asks a user to guess it. The user, should be able to modify the number of attempts at guessing what the number is. The program should tell the user whether the number is lower or greater than the user's guess. When the user guesses the correct answer the program should tell the user he/she had won. At the end of this exchange, your program should print out how many guesses it took to get the number.
# Use the following code snippet to create the random number:   NUMBER = random.randint(MINIMUM, MAXIMUM)
import random

def thinkingOfANumber():
  initInputComplete = False
  numberOfGuesses = int
  guessCount = 0
  NUMBER = random.randint(0, 100)
  # input number of guesses with error handeling
  while initInputComplete == False:
    try:
      numberOfGuesses = int(input("Please enter the number of guesses that your would like :"))
      if isinstance(numberOfGuesses, int) is False or numberOfGuesses < 1:
        raise Exception
    except Exception:
      print("Please be sure to make your input as a positive integer number!")
    else:
      initInputComplete = True
  # input guesses with error handeling
  while guessCount < numberOfGuesses:
    try:
      guess = int(input("Please enter your guess :"))
      if isinstance(numberOfGuesses, int) is False or numberOfGuesses < 1:
        raise Exception
    except Exception:
      print("Please be sure to make your input as a positive integer number!")
    else:
      guessCount += 1
      if guess == NUMBER:
        return print("You win! With a total number of " + str(guessCount) + " guesses.")
      if guess > NUMBER:
        print("The number is lower!")
      if guess < NUMBER:
        print("The number is higher!")
  print("Sorry you ran out of guesses!")
thinkingOfANumber()
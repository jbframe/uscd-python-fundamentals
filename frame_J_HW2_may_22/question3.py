#!/usr/bin/env python
# Assignment 2
# Question 3
# Create a program that will play the “hearts and spades” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number (0000 - 9999) where the numbers should not repeat. For every digit that the user guessed correctly in the correct place, they have a “heart”. For every digit the user guessed correctly in the wrong place is a “spade.” Every time the user makes a guess, tell them how many “hearts” and “spades” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
# Say the number generated by the computer is 1035. An example interaction could look like this:
# Welcome to the Hearts and Spades Game!
# Enter a number:
# >>> 1234
# 2 heart, 0 spades
# >>> 1256
# 1 heart, 1 spade
# ...
import random
def heartsAndSpades():
  guessCount = 0
  guesses = list()
  print("Welcome to the Hearts and Spades Game!")
  NUMBERList = list()
  for i in range(4):
    NUMBERList.append(str(random.randint(0, 9)))
  print(NUMBERList)
  while True:
    try:
      guess = input("Enter a number:")
      if isinstance(int(guess), int) is not True or int(guess) < 0 or len(guess) != 4 or guess in guesses:
        raise Exception
    except Exception:
      print("Please be sure to make your guess a 4-digit integer number (0000 - 9999) and don't repeat guesses!")
    else:
      guesses.append(guess)
      hearts = 0
      spades = 0
      guessCount += 1
      # print('Random number', NUMBERList)
      # Check hearts
      heartDigitsList = [0,0,0,0]
      for i in range(4):
        if NUMBERList[i] == guess[i]:
          hearts += 1
          heartDigitsList[i] = 1
      # Check spades
      spadeDigitsList = [0,0,0,0]
      # iterate over numberlist to see if guess digits are present (do not check digits that are already spades or hearts)
      for i in range(4):
        # continue if numberlist digit (variable i) is a heart
        if heartDigitsList[i] == 1:
          continue
        # iterate over guess digits to see if they match NUMBERList[i]
        for j in range(4):
          # continue if numberlist digit (variable i) is a spade
          if spadeDigitsList[i] == 1:
            continue
          # if guess digit is in the numberList, store the postion of the number list spade so it isn't double counted next time
          if guess[j] == NUMBERList[i]:
            spades += 1
            heartDigitsList[i] = 1
      print(str(hearts) + ' hearts, ' + str(spades) + ' spades')
      # if a digit is a heart it can't also be a spade
      if hearts == 4:
        return print('You won in ' + str(guessCount) + ' guesses!')
heartsAndSpades()
# eg number 1 4 3 2 & guess 4 2 8 8 , expected spades = 2, hearts = 0
# eg number 7 6 3 2 & guess 4 7 8 7 , expected spades = 1, hearts = 0
# eg number 7 7 3 2 & guess 4 1 8 7 , expected spades = 1, hearts = 0
# eg number 7 7 3 2 & guess 7 1 8 7 , expected spades = 1, hearts = 1
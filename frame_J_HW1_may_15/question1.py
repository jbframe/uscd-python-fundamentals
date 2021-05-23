#!/usr/bin/env python
# Assignment 1
# Question 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
def calcYearWhen100(currentYear):
  userName = input("Please enter your name: ")
  while True:
    try:
      userAge = int(input("Please enter how old you will be after your birthday this year: "))
    except ValueError:
      print("Please make sure to enter your age as a number!")
    else:
      yearBorn = currentYear - userAge
      result = yearBorn + 100
      return print(userName + " you will turn 100 years old in the year " + str(result) + ".")

calcYearWhen100(2021)
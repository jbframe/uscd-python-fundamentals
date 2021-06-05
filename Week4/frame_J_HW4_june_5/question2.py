#!/usr/bin/env python
# Assignment 4
# Question 2
# The Luhn algorithm is used to verify whether a credit card number is valid or not. You will need to create a program that uses regular expressions to find the credit card information from a string and then runs the Luhn Algorithm to verify the credit card number. Use the test below.

# "Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."

# The Luhn algorithm is as follows:

# Assume you have a number as: 3 - 7 - 5 - 6 - 2 - 1 - 9 - 8 - 6 - 7 - 3
# Now starting from the rightmost digit i.e. check digit, double every second digit. New number will be: 3 - 14 - 5 - 12 - 2 - 2 - 9 - 16 - 6 - 14 - 3
# If double of a digit is more then 9, then subtract 9 to that number. Then add the digits so the number will become: 3 - 5 - 5 - 3 - 2 - 2 - 9 - 7 - 6 - 5 - 3
# Sum all the numbers together and find the modulus (%10). If the modulus is equal to zero, the number is valid
import re

def verifyCreditCardNumber(string):
  # Pull out the string
  arrayOfNumbersInString = re.findall('[0-9]+', string)
  ccNumberString = ''
  # Assuming credit cards have a min of 12 digits and there could be 4 digit CVS numbers
  for i in arrayOfNumbersInString:
    if len(i) > 4:
      ccNumberString = i
  if (len(ccNumberString) <= 4):
    return "The card number is invalid"

  # Apply Luhn!
  cardNumberLen = int(len(ccNumberString))
  digitsSum = 0
  isSecondDigit = False

  for i in range(cardNumberLen - 1, -1, -1):
    digit = int(ccNumberString[i])
    digitForSum = digit
    if (isSecondDigit == True):
      digitDouble = digit * 2
      if (digitDouble > 9):
        digitForSum = digitDouble - 9
      else:
        digitForSum = digitDouble
    digitsSum += digitForSum
    isSecondDigit = not isSecondDigit
  if (digitsSum % 10 == 0):
    return "The card number is valid"
  else:
    return "The card number is invalid"


testString1 = "Please use my credit card number. It is Visa # 37562198673 with an expiration date of 08/19/2030. The CVS number is 854."

testString2 = "1"

print(verifyCreditCardNumber(testString1)) # Expected "The card number is valid"
print(verifyCreditCardNumber(testString2)) # Expected "The card number is invalid"
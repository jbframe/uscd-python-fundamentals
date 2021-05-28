#!/usr/bin/env python
# Assignment 3
# Question 2
# Write a program that inherits from the class below and adds a modulus division function to the child class (test your code by creating and object and printing out the results for each function):
class Calc():
  def add(self, a, b):
    return  a + b

  def subtract(self, a, b):
    return a - b

  def multiply(self,a,b):
    return a * b

  def divide(self, a, b):
    if b==0:
      raise ValueError('Cannot divide by zero!')
    return a / b

class Modulus(Calc):
  def modulus(self, a, b):
    return  a % b

instanceOfModulusClass = Modulus()
print(instanceOfModulusClass.add(10,2)) # Expect 12
print(instanceOfModulusClass.subtract(10,2)) # Expect 8
print(instanceOfModulusClass.multiply(10,2)) # Expect 20
print(instanceOfModulusClass.divide(10,2)) # Expect 5.0
print(instanceOfModulusClass.modulus(10,2)) # Expect 0
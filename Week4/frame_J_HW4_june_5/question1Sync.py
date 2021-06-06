#!/usr/bin/env python
# Assignment 4
# Question 1
# Write a Python multiprocessing program that runs all five functions below. Use a time.counter to tests the amount of time it takes all functions to run synchronously and then concurrently
# Note: As a more advanced example of multiprocessing you may want to check the following file: ImageProcessingExample
import time
import multiprocessing

startSync = time.perf_counter()
def add(x, y):
  time.sleep(1)
  return x + y

def subtract(x, y):
  time.sleep(1)
  return x-y

def multiply(x, y):
  time.sleep(1)
  return x * y

def divide(x, y):
  time.sleep(1)
  if y==0:
      raise ValueError('Cannot divide by zero!')
  return x / y

def modulus(x, y):
  time.sleep(1)
  return x % y

x = 1000000000
y = 123456789123456789
add(x,y)
subtract(x,y)
multiply(x,y)
divide(x,y)
modulus(x,y)
finishSync = time.perf_counter()
print("Finished synchronsly in ", round(finishSync - startSync, 3), ' seconds')
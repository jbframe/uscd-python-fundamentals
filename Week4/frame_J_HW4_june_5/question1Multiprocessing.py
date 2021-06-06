#!/usr/bin/env python
# Assignment 4
# Question 1
# Write a Python multiprocessing program that runs all five functions below. Use a time.counter to tests the amount of time it takes all functions to run synchronously and then concurrently
# Note: As a more advanced example of multiprocessing you may want to check the following file: ImageProcessingExample
import time
import multiprocessing

start = time.perf_counter()
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

if __name__ == '__main__':
  x = 1000000000
  y = 123456789123456789
  process1 = multiprocessing.Process(target = add, args = (x, y))
  process2 = multiprocessing.Process(target = subtract, args = (x, y))
  process3 = multiprocessing.Process(target = multiply, args = (x, y))
  process4 = multiprocessing.Process(target = divide, args = (x, y))
  process5 = multiprocessing.Process(target = modulus, args = (x, y))

  process1.start()
  process2.start()
  process3.start()
  process4.start()
  process5.start()

  process1.join()
  process2.join()
  process3.join()
  process4.join()
  process5.join()

  finish = time.perf_counter()
  print("Finished multiprocessing in ", round(finish-start, 3), ' seconds')


# Python Iterators

class IteratorNumbers:
# The __iter__() method is similar to __init__(), you can do operations (initializing etc.), but must always return the iterator object itself.
  def __iter__(self):
    self.curNumber = 1
    return self

#The __next__() method also allows you to do operations, and must return the next item in the sequence.
  def __next__(self):
    nextNumber = self.curNumber
    self.curNumber += 1
    return nextNumber

iteratorClassObject = IteratorNumbers()
myIterator = iter(iteratorClassObject)

print(next(myIterator)) # Expected 1
print(next(myIterator)) # Expected 2
print(next(myIterator)) # Expected 3
print(next(myIterator)) # Expected 4
print(next(myIterator)) # Expected 5

#Python Generators

#The yield statement used in generators suspends a function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run.
class GeneratorNumbers:
  def __iter__(self):
    self.curNumber = 1
    while True:
      yield self.curNumber
      self.curNumber += 1

generatorClassObject = GeneratorNumbers()
myGenerator = iter(generatorClassObject)

print(next(myGenerator)) # Expected 1
print(next(myGenerator)) # Expected 2
print(next(myGenerator)) # Expected 3
print(next(myGenerator)) # Expected 4
print(next(myGenerator)) # Expected 5
# We covered pickling and unpickling in these week's lectures. Now that we know how to use the pickle library do some research and compare pickle with cpickle. Also do some research on the dill library. Compare and explain the benefits and write an example for each.

import pickle
import _pickle as cPickle
import dill

# Per the lecture, pickle serializes or un-serializes Python objects into a series of bytes.
dict = {'pickle': 'python based', 'cpickle':'c based', 'dill':''}
#Pickle Example

def pickleFile():
  filename = 'pickle'
  fhandle = open(filename, 'wb')
  pickle.dump(pickle, fhandle)
  fhandle.close()
pickleFile()

def unpickleFile():
  filename = 'pickle'
  infile = open(filename, 'rb')
  newDict = pickle.load(infile)
  infile.close()
  print(newDict)
unpickleFile() # Expected output {'pickle': 'python based', 'cpickle':'c based', 'dill':''}


# CPickle completes the same process but in C, so it is much faster
#CPickle Example

def CpickleFile():
  filename = 'cpickle'
  fhandle = open(filename, 'wb')
  cPickle.dump(cpickle, fhandle)
  fhandle.close()
CpickleFile()

def CunpickleFile():
  filename = 'cpickle'
  infile = open(filename, 'rb')
  newDict = cPickle.load(infile)
  infile.close()
  print(newDict)
CunpickleFile() # Expected output {'pickle': 'python based', 'cpickle':'c based', 'dill':''}

# Dill is very similar to CPickle, however it also let's you serialize nested functions, geneators and lambda functions.

xplusone = lamdbda x: x + 1
myDill = dill.dumps(xplusone)

unDill = dill.loads(myDill)(5)
print(unDill) #Expected output > 6
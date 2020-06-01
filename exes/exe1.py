import numpy

def f(x):
  return x - numpy.cos(x)

def Df(x):
  return 1 + numpy.sin(x)

def D2f(x):
  return numpy.cos(x)



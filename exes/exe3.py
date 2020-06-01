import math
import numpy

def f(x):
  return math.e ** x - numpy.cos(x)

def Df(x):
  return math.e ** x + numpy.sin(x)

def D2f(x):
  return math.e ** x + numpy.cos(x)
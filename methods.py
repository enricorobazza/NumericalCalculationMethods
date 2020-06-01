import math
import numpy as np

N = 100000

def convergenceOrder(e):
    p = [None]
    for k in range(1, len(e)-1):
      try:
        p.append(math.log(e[k+1]/e[k])/math.log(e[k]/e[k-1]))
      except:
        p.append(None)
    if(len(p) == 0):
      return math.inf
    p.append(None)
    return p 

def newton(f, Df, x0, abs_tol):
  xk = x0
  xk_1 = None
  iterations = [xk]
  for k in range(0, N):
    fxk = f(xk)
    if xk_1 != None and abs(xk - xk_1) < abs_tol:
      return iterations
    Dfxk = Df(xk)
    if Dfxk == 0:
      return []
    xk_1 = xk
    xk = xk - fxk/Dfxk
    iterations.append(xk)
  return iterations

def halley(f, Df, D2f, x0, abs_tol):
  xk = x0
  xk_1 = None
  iterations = [xk]
  for k in range(0,N):
    fxk = f(xk)
    if xk_1 != None and abs(xk - xk_1) < abs_tol:
      return iterations
    xk_1 = xk
    try:
      xk = xk - fxk * Df(xk) / (Df(xk)**2 - 1/2 * fxk * D2f(xk))
    except:
      return []
    iterations.append(xk)
  return iterations

def bisection(f, a, b, abs_tol):
  iterations = []
  for k in range(0, N):
    c = (a+b)/2
    iterations.append(c)
    if(f(c) == 0 or abs(b-a)/2 < abs_tol):
      return iterations
    if(f(c) * f(a) >= 0):
      a = c
    else:
      b = c
  return iterations

def secant(f, x0, x1, abs_tol):
  k = 1
  fx0 = f(x0)
  fx1 = f(x1)
  iterations = []
  while(abs(x1 - x0) > abs_tol and k < N):
    try:
      xk = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    except:
      return []
    x0 = x1
    x1 = xk
    fx0 = fx1
    fx1 = f(x1)
    iterations.append(xk)
    k += 1
  return iterations
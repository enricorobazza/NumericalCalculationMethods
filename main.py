import methods
import numpy
from exes import exe1, exe2, exe3
import csv

debug = False
def info(text):
  if(debug):
    print(text)

def get_abs(i, x):
  return numpy.array([abs(iteration - x) for iteration in i])

def write_result(writer, method, i, p):
  for x in range(len(i)):
    i_str = "%.16f" % i[x] if i[x] != None else ""
    p_str = "%.16f" % p[x] if p[x] != None else ""
    writer.writerow([method, i_str.replace('.', ','), p_str.replace('.', ',')])

def run_all_methods(file, f, Df, D2f, a, b, x):
  csv_file = open('%s.csv'%file, mode='w')
  writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['Method', 'Iteration', 'Convergence'])

  i = methods.newton(f, Df, a, 10**(-16))
  p = methods.convergenceOrder(get_abs(i, x))
  write_result(writer, 'Newton', i, p)
  print("Newton found solution:", i[-1], "in", len(i), "iterations")

  i = methods.halley(f, Df, D2f, a, 10**(-16))
  p = methods.convergenceOrder(get_abs(i, x))
  write_result(writer, 'Halley', i, p)
  print("Halley found solution:", i[-1], "in", len(i), "iterations")

  i = methods.bisection(f, b, a, 10**(-16))
  p = methods.convergenceOrder(get_abs(i, x))
  write_result(writer, 'Bisection', i, p)
  print("Bisection found solution:", i[-1], "in", len(i), "iterations")

  i = methods.secant(f, b, a, 10**(-16))
  p = methods.convergenceOrder(get_abs(i, x))
  write_result(writer, 'Secant', i, p)
  print("Secant found solution:", i[-1], "in", len(i), "iterations")
  

run_all_methods('exe1',exe1.f, exe1.Df, exe1.D2f, 1.5, 0, 0.739085133)
print("")
run_all_methods('exe2', exe2.f, exe2.Df, exe2.D2f, -2, 7.5, 3)
print("")
run_all_methods('exe3', exe3.f, exe3.Df, exe3.D2f, 3, -0.5, 0)
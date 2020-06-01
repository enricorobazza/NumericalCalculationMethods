import methods
import numpy
from exes import exe1, exe2, exe3


abs_tol = 10**(-16)

## EXE1

# (solution, iterations) = methods.newton(exe1.f, exe1.Df, 1.5, abs_tol)
# print(solution, len(iterations), "\n", iterations)

# (solution, iterations) = methods.bisection(exe1.f, 0, 1.5, abs_tol)
# print(solution, len(iterations), "\n", iterations)

# (solution, iterations) = methods.halley(exe1.f, exe1.Df, exe1.D2f, 1.5, abs_tol)
# print(solution, len(iterations), "\n", iterations)

# (solution, iterations) = methods.secant(exe1.f, 0, 1.5, abs_tol)
# print(solution, len(iterations), "\n", iterations)


## EXE2

# (solution, iterations) = methods.newton(exe2.f, exe2.Df, 7, abs_tol)
# print(solution, len(iterations), "\n")

# (solution, iterations) = methods.bisection(exe2.f, -2, 7, abs_tol)
# print(solution, len(iterations), "\n")

# (solution, iterations) = methods.halley(exe2.f, exe2.Df, exe2.D2f, 7, abs_tol)
# print(solution, len(iterations), "\n")

(solution, iterations) = methods.secant3(exe2.f, -2, 7, abs_tol)
print(solution, len(iterations), "\n")
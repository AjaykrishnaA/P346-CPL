import myLibrary as Lib
import matplotlib.pyplot as plt


def f(x): return 4/(1+x**2)


a = 0
b = 1

Res = Lib.integ_MonteCarlo(f, a, b, 500, 10, 10)


# For plotting:

x = Res[1]
y = Res[2]

plt.plot(x, y)
plt.title("\u03C0 vs Monte Carlo Integration result")
plt.xlabel("Sample size -->")
plt.ylabel("Integration value -->")

plt.show()

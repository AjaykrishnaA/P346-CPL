import math
import myLibrary as Lib
import matplotlib.pyplot as plt

accuracy = 10**(-5)


def f(x):
    return (math.log(x/2) - math.sin(5*x/2))


print(Lib.bisection(f, 1, 2, accuracy))


""" # For plotting:
plt.subplot(2, 1, 1)
plt.plot(range(1, required_n(test_val)+4), err_sin)
plt.title("SIN("+str(test_val)+")")
plt.xlabel("No. of Iterations")
plt.ylabel("Error")

plt.subplot(2, 1, 2)
plt.plot(range(1, required_n(test_val)+4), err_exp)
plt.title("EXP("+str(-test_val)+")")
plt.xlabel("No. of Iterations")
plt.ylabel("Error")

plt.suptitle("Error v/s No. of Iterations for x="+str(test_val))
plt.show() """

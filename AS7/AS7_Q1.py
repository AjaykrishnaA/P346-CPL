import myLibrary as Lib
import matplotlib.pyplot as plt
import math


def f(y, x):
    return (y*math.log(y))/x


x, y = Lib.forward_euler(f, 2.71828, 2, 10, 0.5)
print(x, y)


# For plotting:

plt.plot(x, y)
plt.title("Forward Euler Result")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

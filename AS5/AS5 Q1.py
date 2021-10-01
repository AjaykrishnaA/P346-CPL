import math
import myLibrary as Lib
import matplotlib.pyplot as plt
from tabulate import tabulate

accuracy = 10**(-5)
a = 1.6
b = 2.4


def f(x):
    return (math.log10(x/2) - math.sin(5*x/2))


bis = Lib.bisection(f, a, b, accuracy)
regF = Lib.regulaFalsi(f, a, b, accuracy)
print("\n")
print("The root using the Bisection method is:")
print(bis[0])
print("The root using the Regula Falsi method is:")
print(regF[0])


# For plotting:
plt.subplot(2, 1, 1)

x_bis = range(1, bis[1]+1)
y_bis = bis[2]

plt.plot(x_bis, y_bis)
plt.title("Bisection")
plt.xlabel("No. of Iterations")
plt.ylabel("|Function Value|")

plt.subplot(2, 1, 2)

x_regF = range(1, regF[1]+1)
y_regF = regF[2]

plt.plot(x_regF, y_regF)
plt.title("Regula Falsi")
plt.xlabel("No. of Iterations")
plt.ylabel("|Function Value|")

plt.suptitle("Convergence : Comparison")
plt.show()


# For table:

# 1.
print("\nTable showing Bisection root convergence:\n")
l = [[i, bis[3][i-1]] for i in x_bis]
table = tabulate(l, headers=['#Iterations', 'Root'], tablefmt='orgtbl')
print(table)

# 2.
print("\nTable showing Regula Falsi root convergence:\n")
l = [[i, regF[3][i-1]] for i in x_regF]
table = tabulate(l, headers=['#Iterations', 'Root'], tablefmt='orgtbl')
print(table)


#################################### OUTPUT ####################################
""" 

The root using the Bisection method is:
2.5559669494628903
The root using the Regula Falsi method is:
2.555965092756274

Table showing Bisection root convergence:

|   #Iterations |    Root |
|---------------+---------|
|             1 | 2.6     |
|             2 | 2.1     |
|             3 | 2.35    |
|             4 | 2.475   |
|             5 | 2.5375  |
|             6 | 2.56875 |
|             7 | 2.55312 |
|             8 | 2.56094 |
|             9 | 2.55703 |
|            10 | 2.55508 |
|            11 | 2.55605 |
|            12 | 2.55557 |
|            13 | 2.55581 |
|            14 | 2.55593 |
|            15 | 2.55599 |
|            16 | 2.55596 |
|            17 | 2.55598 |
|            18 | 2.55597 |
|            19 | 2.55597 |

Table showing Regula Falsi root convergence:

|   #Iterations |    Root |
|---------------+---------|
|             1 | 3.21592 |
|             2 | 2.34236 |
|             3 | 2.67737 |
|             4 | 2.55664 |
|             5 | 2.55595 |
|             6 | 2.55597 |
|             7 | 2.55597 |

"""

import math
import myLibrary as Lib
import matplotlib.pyplot as plt
from tabulate import tabulate

accuracy = 10**(-4)
# Initial bracket for both Bisection (Midpoint) and Regula Falsi:
a = 0
b = 1

# Define the input the function here:

#AjaykrishnaA 1911017
def f(x):
    return 4*math.exp(-x)*math.sin(x)-1


bis = Lib.bisection(f, a, b, accuracy)
regF = Lib.regulaFalsi(f, a, b, accuracy)
print("\n")
print("The root using the Bisection (Midpoint) method is:")
print(bis[0])
print("The root using the Regula Falsi method is:")
print(regF[0])
#AjaykrishnaA 1911017

# For plotting:
plt.subplot(2, 1, 1)

x_bis = range(1, bis[1]+1)
y_bis = bis[2]

plt.plot(x_bis, y_bis)
plt.title("Bisection (Midpoint)")
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

#AjaykrishnaA 1911017
# For table:

# 1.
print("\nTable showing Bisection (Midpoint) root convergence:\n")
l = [[i, bis[3][i-1]] for i in x_bis]
table = tabulate(l, headers=['#Iterations', 'Root'],
                 tablefmt='orgtbl', floatfmt="")
print(table)

# 2.
print("\nTable showing Regula Falsi root convergence:\n")
l = [[i, regF[3][i-1]] for i in x_regF]
table = tabulate(l, headers=['#Iterations', 'Root'],
                 tablefmt='orgtbl', floatfmt="")
print(table)


#################################### OUTPUT ####################################
""" 

The root using the Bisection (Midpoint) method is:
0.37054443359375
The root using the Regula Falsi method is:
0.370562300835524

Table showing Bisection (Midpoint) root convergence:

|   #Iterations |             Root |
|---------------+------------------|
|             1 | 0.5              |
|             2 | 0.25             |
|             3 | 0.375            |
|             4 | 0.3125           |
|             5 | 0.34375          |
|             6 | 0.359375         |
|             7 | 0.3671875        |
|             8 | 0.37109375       |
|             9 | 0.369140625      |
|            10 | 0.3701171875     |
|            11 | 0.37060546875    |
|            12 | 0.370361328125   |
|            13 | 0.3704833984375  |
|            14 | 0.37054443359375 |

Table showing Regula Falsi root convergence:

|   #Iterations |                Root |
|---------------+---------------------|
|             1 | 0.8075982052665829  |
|             2 | 0.6265494882844935  |
|             3 | 0.49985393187801186 |
|             4 | 0.42979553644622137 |
|             5 | 0.39632542281599925 |
|             6 | 0.3814972968627457  |
|             7 | 0.3751529050070425  |
|             8 | 0.3724793039057679  |
|             9 | 0.3713598671047275  |
|            10 | 0.3708924286491957  |
|            11 | 0.37069746366711326 |
|            12 | 0.37061618376611605 |
|            13 | 0.37058230528185915 |
|            14 | 0.37056818546599873 |
|            15 | 0.370562300835524   |

"""

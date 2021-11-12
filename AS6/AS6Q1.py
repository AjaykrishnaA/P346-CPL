import myLibrary as Lib
from tabulate import tabulate

N = [8, 16, 24]


def f(x): return (1+1/x)**(1/2)


a = 1
b = 4

analy_res = 3.620184280785752
# For table:
print("\nTable comparing results obtained with numerical integration methods:\n")
print("Analytical result = ", analy_res, "\n")
l = [[N[i], Lib.integ_Midpoint(f, a, b, N[i]), abs(Lib.integ_Midpoint(f, a, b, N[i])-analy_res), Lib.integ_Trapezoidal(f, a, b, N[i]), abs(
    Lib.integ_Trapezoidal(f, a, b, N[i])-analy_res), Lib.integ_Simpsons(f, a, b, N[i]), abs(Lib.integ_Simpsons(f, a, b, N[i])-analy_res)] for i in range(3)]
table = tabulate(l, headers=["Iterations", "Midpoint", "Error", "Trapezoidal", "Error", "Simpsons", "Error"],
                 tablefmt='orgtbl', floatfmt=".8f")
print(table)

############################## OUTPUT ##############################
"""

Table comparing results obtained with numerical integration methods:

Analytical result =  3.620184280785752

|   Iterations |   Midpoint |      Error |   Trapezoidal |      Error |   Simpsons |      Error |
|--------------+------------+------------+---------------+------------+------------+------------|
|            8 | 3.61831386 | 0.00187042 |    3.62395695 | 0.00377267 | 3.62019489 | 0.00001061 |
|           16 | 3.61970976 | 0.00047452 |    3.62113540 | 0.00095112 | 3.62018498 | 0.00000070 |
|           24 | 3.61997279 | 0.00021150 |    3.62060769 | 0.00042341 | 3.62018442 | 0.00000014 |


"""

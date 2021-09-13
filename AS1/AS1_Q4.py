# This is an interactive program.
# To find sin(x) and exp(-x) numerically upto 4 places in decimal and plot the error v/s iteration no. graph.
from math import sin, exp
import matplotlib.pyplot as plt


def my_factorial(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact


def my_sin(x, n: int):
    s = 0
    for i in range(n):
        a_n = ((-1)**(i))*x**(2*i+1)/my_factorial(2*i+1)  # n_th term
        s = s + a_n
    return s


def my_exp_minus(x, n: int):
    s = 0
    for i in range(n):
        a_n = ((-1)**(i))*x**(i)/my_factorial(i)  # n_th term
        s = s + a_n
    return s


# Taking input from user
# Empty input will attach "1.0" to the input
test_val = float(input("Type a number: ") or "0.3")
print("Input test value is: ", str(test_val)+".")


def required_n(x):
    eps = 10**(-5)
    n = 1
    while abs(my_exp_minus(test_val, n)-exp(-test_val)) > eps or abs(my_sin(test_val, n)-sin(test_val)) > eps:
        n += 1
    return n


print("required n: ", required_n(test_val))

err_sin = []
err_exp = []

print("################ SIN ################")
print("Iteration No.", "Error")
for i in range(1, required_n(test_val)+4):
    # List appending for plotting
    err_sin.append(abs(my_sin(test_val, i)-sin(test_val)))
    # printing data for text output
    print(i, "           ", abs(my_sin(test_val, i)-sin(test_val)))

print("################ EXP ################")
print("Iteration No.", "Error")
for i in range(1, required_n(test_val)+4):
    # List appending for plotting
    err_exp.append(abs(my_exp_minus(test_val, i)-exp(-test_val)))
    # printing data for text output
    print(i, "           ", abs(my_exp_minus(test_val, i)-exp(-test_val)))

# For plotting:
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
plt.show()


#################################### OUTPUT ####################################

"""

Type a number: .4
Input test value is:  0.4.
required n:  6
################ SIN ################
Iteration No. Error
1             0.0105816576913495
2             8.50089753171579e-05
3             3.24358016168258e-07
4             7.213489250368355e-10
5             1.0496603586318543e-12
6             1.1102230246251565e-15
7             5.551115123125783e-17
8             5.551115123125783e-17
9             5.551115123125783e-17
################ EXP ################
Iteration No. Error
1             0.3296799539643607
2             0.07032004603563935
3             0.00967995396436061
4             0.0009867127023061029
5             7.995396436055735e-05
6             5.379368972824317e-06
7             3.095199160307871e-07
8             1.5559449062507724e-08
9             6.945192199125927e-10

"""

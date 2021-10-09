import math
import myLibrary as Lib

accuracy = 10**(-4)
# Initial guess for Newton Raphson:
x = 5
#AjaykrishnaA 1911017
# Define the input the function here:


def f(x):
    return (x-5)*math.exp(x)+5
#AjaykrishnaA 1911017

NR = Lib.newtonRaphson(f, x, accuracy)
root = NR[0]
print("\n")
print("The root, x using the Newton Raphson method is:")
print("{:.5f}".format(root))


h = 6.626*10**(-34)  # in  m^2 kg / s
k = 1.381*10**(-23)  # in m^2 kg s^(-2) K(-1)
c = 3*10**8  # in m/s

print("Hence the value of Wein’s constant, b in meter-kelvin is :")
#AjaykrishnaA 1911017
result = h*c/(k*root)
print("{:.8f}".format(result))


#################################### OUTPUT ####################################
""" 

The root, x using the Newton Raphson method is:
4.96511
Hence the value of Wein’s constant, b in meter-kelvin is :
0.00289901

"""
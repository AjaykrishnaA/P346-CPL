import myLibrary as Lib


def f(x): return x*(1+x)**(1/2)


a = 0
b = 1

Max_Error_Bound = 0.001
N_midpoint = 7
N_trapezoidal = 10
N_simpsons = 3


def integ(method, f, a, b, n):
    if method == "midpoint":
        return Lib.integ_Midpoint(f, a, b, n)
    if method == "trapezoidal":
        return Lib.integ_Trapezoidal(f, a, b, n)
    if method == "simpsons":
        return Lib.integ_Simpsons(f, a, b, n)


print("\nMax Error Bound = ", Max_Error_Bound, "\n")
for i in ["midpoint", "trapezoidal", "simpsons"]:
    print("The numerical integration result using",
          i, "method is:", integ(i, f, a, b, vars()[f"N_"+i]))


############################## OUTPUT ##############################
"""

Max Error Bound =  0.001

The numerical integration result using midpoint method is: 0.643137698010569
The numerical integration result using trapezoidal method is: 0.6444300126935936
The numerical integration result using simpsons method is: 0.6437925869327117


"""

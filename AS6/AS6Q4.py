import myLibrary as Lib


def f(x): return x**3
def g(x): return x**2


a = 0
b = 2
n = 100
Res = Lib.integ_Trapezoidal(f, a, b, n)/Lib.integ_Trapezoidal(g, a, b, n)
print("\nThe centre of mass of the 2 meter long beam having linear mass density λ(x) = x², where x is measured from one of the ends is at", Res, "meter")

############################## OUTPUT ##############################
"""

The centre of mass of the 2 meter long beam having linear mass density λ(x) = x², where x is measured from one of the ends is at 1.5000749962501885 
meter


"""
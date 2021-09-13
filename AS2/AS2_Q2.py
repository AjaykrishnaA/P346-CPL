# Defines a class of complex numbers along with functions and operations associated with it.
from math import atan, pi

# Defines the class of complex numbers:


class myComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(str(self.real), "+", str(self.imag)+"i")

    def conjugate(self):
        return(myComplex(self.real, -self.imag))

    def mod(self):
        return float((self.real**2+self.imag**2)**0.5)

    def phase(self):
        if self.real != 0:
            return atan(self.imag/self.real)
        elif self.imag == 0:
            return None
        elif self.imag > 0:
            return pi/2
        else:
            return -pi/2


# Defines operations between two complex numbers:

def cmplxSum(a: myComplex, b: myComplex):
    return myComplex(a.real+b.real, a.imag+b.imag)


def cmplxProduct(a: myComplex, b: myComplex):
    return myComplex(a.real*b.real-a.imag*b.imag, a.real*b.imag+a.imag*b.real)


def cmplxQuotient(a: myComplex, b: myComplex):
    if b.mod() != 0:
        return cmplxProduct(cmplxProduct(a, b.conjugate()), b.mod()**(-2))
    else:
        print("Division is undefined as divisor is zero! Try again with another input.")


init_com = "This program takes two complex numbers given by your input and outputs the result of all the operations with and between them. Note that empty input will attach '1' to the input."
later_com = "Try once more?"
cur_com = init_com

for i in range(7):
    print()
    print(cur_com)
    print()
    # Defines the 1st Complex no. from user input and prints its attributes:
    c1 = myComplex(float(input("Real part of the 1st Complex no. : ") or 1), float(
        input("Imaginary part of the 1st Complex no. : ") or 1))  # Empty input will attach "1" to the input.

    print()
    print("The 1st Complex no. is :", end=" ")
    c1.display()
    print("Conjugate of the 1st :", end=" ")
    c1.conjugate().display()
    print("Modulus of the 1st :", end=" ")
    print(c1.mod())
    print("Phase of the 1st :", end=" ")
    print(c1.phase())
    print()

    # Defines the 2nd Complex no. from user input and prints its attributes:
    c2 = myComplex(float(input("Real part of the 2nd Complex no. : ") or 1), float(
        input("Imaginary part of the 2nd Complex no. : ") or 1))  # Empty input will attach "1" to the input.

    print()
    print("The 2nd Complex no. is :", end=" ")
    c2.display()
    print("Conjugate of the 2nd :", end=" ")
    c2.conjugate().display()
    print("Modulus of the 2nd :", end=" ")
    print(c2.mod())
    print("Phase of the 2nd :", end=" ")
    print(c2.phase())
    print()

    # Prints the result of the various operations between the complex numbers:
    print("Result of the various operations between the complex numbers : ")
    print("Sum of the 1st and 2nd :", end=" ")
    cmplxSum(c1, c2).display()
    print("Product of the 1st and 2nd :", end=" ")
    cmplxProduct(c1, c2).display()
    print("1st Complex number divided by the 2nd :", end=" ")
    if cmplxQuotient(c1, c2)!=None : cmplxQuotient(c1, c2).display()
    print("2nd Complex number divided by the 1st :", end=" ")
    if cmplxQuotient(c2, c1)!=None : cmplxQuotient(c2, c1).display()

    cur_com = later_com



#################################### OUTPUT ####################################

"""

################# 1 ###################
This program takes two complex numbers given by your input and outputs the result of all the operations with and between them. Note that empty input will attach '1' to the input.

Real part of the 1st Complex no. : 1
Imaginary part of the 1st Complex no. : 0

The 1st Complex no. is : 1.0 + 0.0i
Conjugate of the 1st : 1.0 + -0.0i
Modulus of the 1st : 1.0
Phase of the 1st : 0.0

Real part of the 2nd Complex no. : 1
Imaginary part of the 2nd Complex no. : 0

The 2nd Complex no. is : 1.0 + 0.0i
Conjugate of the 2nd : 1.0 + -0.0i
Modulus of the 2nd : 1.0
Phase of the 2nd : 0.0

Result of the various operations between the complex numbers :
Sum of the 1st and 2nd : 2.0 + 0.0i
Product of the 1st and 2nd : 1.0 + 0.0i
1st Complex number divided by the 2nd : 1.0 + 0.0i
2nd Complex number divided by the 1st : 1.0 + 0.0i

Try once more? 

################# 2 ###################

Real part of the 1st Complex no. : 1
Imaginary part of the 1st Complex no. : 0

The 1st Complex no. is : 1.0 + 0.0i
Conjugate of the 1st : 1.0 + -0.0i
Modulus of the 1st : 1.0
Phase of the 1st : 0.0

Real part of the 2nd Complex no. : 0
Imaginary part of the 2nd Complex no. : 1

The 2nd Complex no. is : 0.0 + 1.0i
Conjugate of the 2nd : 0.0 + -1.0i
Modulus of the 2nd : 1.0
Phase of the 2nd : 1.5707963267948966

Result of the various operations between the complex numbers :
Sum of the 1st and 2nd : 1.0 + 1.0i
Product of the 1st and 2nd : 0.0 + 1.0i
1st Complex number divided by the 2nd : 0.0 + -1.0i
2nd Complex number divided by the 1st : 0.0 + 1.0i

Try once more?

################# 3 ###################

Real part of the 1st Complex no. : 1
Imaginary part of the 1st Complex no. : 1

The 1st Complex no. is : 1.0 + 1.0i
Conjugate of the 1st : 1.0 + -1.0i
Modulus of the 1st : 1.4142135623730951
Phase of the 1st : 0.7853981633974483

Real part of the 2nd Complex no. : 1
Imaginary part of the 2nd Complex no. : -1

The 2nd Complex no. is : 1.0 + -1.0i
Conjugate of the 2nd : 1.0 + 1.0i
Modulus of the 2nd : 1.4142135623730951
Phase of the 2nd : -0.7853981633974483

Result of the various operations between the complex numbers :
Sum of the 1st and 2nd : 2.0 + 0.0i
Product of the 1st and 2nd : 2.0 + 0.0i
1st Complex number divided by the 2nd : 0.0 + 0.9999999999999999i
2nd Complex number divided by the 1st : 0.0 + -0.9999999999999999i

Try once more?

################# 4 ###################

Real part of the 1st Complex no. : 0
Imaginary part of the 1st Complex no. : 0

The 1st Complex no. is : 0.0 + 0.0i
Conjugate of the 1st : 0.0 + -0.0i
Modulus of the 1st : 0.0
Phase of the 1st : None

Real part of the 2nd Complex no. : 1
Imaginary part of the 2nd Complex no. : 1

The 2nd Complex no. is : 1.0 + 1.0i
Conjugate of the 2nd : 1.0 + -1.0i
Modulus of the 2nd : 1.4142135623730951
Phase of the 2nd : 0.7853981633974483

Result of the various operations between the complex numbers :
Sum of the 1st and 2nd : 1.0 + 1.0i
Product of the 1st and 2nd : 0.0 + 0.0i
1st Complex number divided by the 2nd : 0.0 + 0.0i
2nd Complex number divided by the 1st : Division is undefined as divisor is zero! Try again with another input.

Try once more?

################# 5 ###################

Real part of the 1st Complex no. : 3
Imaginary part of the 1st Complex no. : 4

The 1st Complex no. is : 3.0 + 4.0i
Conjugate of the 1st : 3.0 + -4.0i
Modulus of the 1st : 5.0
Phase of the 1st : 0.9272952180016122

Real part of the 2nd Complex no. : 4
Imaginary part of the 2nd Complex no. : -3

The 2nd Complex no. is : 4.0 + -3.0i
Conjugate of the 2nd : 4.0 + 3.0i
Modulus of the 2nd : 5.0
Phase of the 2nd : -0.6435011087932844

Result of the various operations between the complex numbers :
Sum of the 1st and 2nd : 7.0 + 1.0i
Product of the 1st and 2nd : 24.0 + 7.0i
1st Complex number divided by the 2nd : 0.0 + 1.0i
2nd Complex number divided by the 1st : 0.0 + -1.0i

"""

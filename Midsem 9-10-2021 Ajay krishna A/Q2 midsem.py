import myLibrary as Lib

#AjaykrishnaA 1911017
mat = Lib.getMatFromFile("Q2mat")
Inverse = Lib.gjInverse(mat)

print("Input matrix is :")
Lib.displayMat(mat)
print("\nInverse of the input matrix after GaussJordan Elimination is:")
Lib.displayMat(Inverse)

#AjaykrishnaA 1911017

# For checking if inverse is correct:
Product = Lib.matMult(mat, Inverse)
print("Product of the input and inverse matrices is :")
Lib.displayMat(Product)
print("Identity matris of the same order is :")
I = Lib.Identity(len(mat))
Lib.displayMat(I)
print("Checking...\n")
if Product == I:
    print("The product of input matrix and it's inverse is indeed the identity matris of the same order. Hence the inverse exists and is correct.")
else:
    print("The inverse is wrong!")
#AjaykrishnaA 1911017
#################################### OUTPUT ####################################

"""      

Input matrix is :
[0.0, 0.0, 0.0, 2.0]
[0.0, 0.0, 3.0, 0.0]
[0.0, 4.0, 0.0, 0.0]
[5.0, 0.0, 0.0, 0.0]


Inverse of the input matrix after GaussJordan Elimination is:
[0.0, 0.0, 0.0, 0.2]
[0.0, 0.0, 0.25, 0.0]
[0.0, 0.33, 0.0, 0.0]
[0.5, 0.0, 0.0, 0.0]

Product of the input and inverse matrices is :
[1.0, 0.0, 0.0, 0.0]
[0.0, 1.0, 0.0, 0.0]
[0.0, 0.0, 1.0, 0.0]
[0.0, 0.0, 0.0, 1.0]

Identity matris of the same order is :
[1.0, 0.0, 0.0, 0.0]
[0.0, 1.0, 0.0, 0.0]
[0.0, 0.0, 1.0, 0.0]
[0.0, 0.0, 0.0, 1.0]

Checking...

The product of input matrix and it's inverse is indeed the identity matris of the same order. Hence the inverse exists and is correct.



"""

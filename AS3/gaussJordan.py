from myLibrary import (getMatFromFile,
displayMat,
swapRows,
partialPivot,
guassJordan,
solve,
gjInverse,
gjDeterminant)


mat1 = getMatFromFile("mat1")
mat2 = getMatFromFile("mat2")
mat3 = getMatFromFile("mat3")
mat4 = getMatFromFile("mat4")


print("\n######################## Answer 1 ########################")
solve(mat1, 4, 5)
print("\n######################## Answer 2 ########################")
solve(mat2, 3, 4)
print("\n######################## Answer 3 ########################")
gjInverse(mat3)
print("\n######################## Answer 4 ########################")
print("Determinant of your input matrix is: ", gjDeterminant(mat4, 4))
print("\n")

#################################### OUTPUT ####################################

"""

######################## Answer 1 ########################       

Your input system of equations in augmented matrix format is:    
[1.0, 1.0, 1.0, 1.0, 13.0]
[2.0, 3.0, 0.0, -1.0, -1.0]
[-3.0, 4.0, 1.0, 2.0, 10.0]
[1.0, 2.0, -1.0, 1.0, 1.0]


Your matrix after GaussJordan Elimination is:
[1.0, 0.0, 0.0, 0.0, 2.0]
[0.0, 1.0, 0.0, 0.0, -0.0]
[0.0, 0.0, 1.0, 0.0, 6.0]
[0.0, 0.0, 0.0, 1.0, 5.0]

The solutions are:
x_1 = 2.0
x_2 = -0.0
x_3 = 6.0
x_4 = 5.0

######################## Answer 2 ########################       

Your input system of equations in augmented matrix format is:    
[0.0, 2.0, -3.0, -1.0]
[1.0, 0.0, 1.0, 0.0]
[1.0, -1.0, 0.0, 3.0]


Your matrix after GaussJordan Elimination is:
[1.0, 0.0, 0.0, 1.0]
[0.0, 1.0, 0.0, -2.0]
[0.0, 0.0, 1.0, -1.0]

The solutions are:
x_1 = 1.0
x_2 = -2.0
x_3 = -1.0

######################## Answer 3 ########################       

Your input matrix for finding inverse is:
[0.0, 2.0, 1.0]
[4.0, 0.0, 1.0]
[-1.0, 2.0, 0.0]

The augmented matrix is :
[0.0, 2.0, 1.0, 1.0, 0.0, 0.0]
[4.0, 0.0, 1.0, 0.0, 1.0, 0.0]
[-1.0, 2.0, 0.0, 0.0, 0.0, 1.0]


Your matrix after GaussJordan Elimination is:
[1.0, 0.0, 0.0, -0.33, 0.33, 0.33]
[0.0, 1.0, 0.0, -0.17, 0.17, 0.67]
[0.0, 0.0, 1.0, 1.33, -0.33, -1.33]

Hence, the solution is:
[-0.33, 0.33, 0.33]
[-0.17, 0.17, 0.67]
[1.33, -0.33, -1.33]


######################## Answer 4 ########################       

Your input matrix for finding determinant is:
[1.0, 4.0, 2.0, 3.0]
[0.0, 1.0, 4.0, 4.0]
[-1.0, 0.0, 1.0, 0.0]
[2.0, 0.0, 4.0, 1.0]

Determinant of your input matrix is:  65.0

"""

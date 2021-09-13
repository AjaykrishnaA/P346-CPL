from myLibrary import (getMatFromFile,
                       displayMat,
                       solve_LU)

# augmented matrix:
Mat = getMatFromFile("q3mat")
vec = [2.20, 2.85, 2.79, 2.87]

b = [[vec[i]] for i in range(len(vec))]
print("\nThe coefficient matrix is:")
displayMat(Mat)
print("The constant matrix is:")
displayMat(b)
print("\nSolution using cholesky : ")
solve_LU(Mat, b, 4, "cholesky")
print("\n")

#################################### OUTPUT ####################################
""" 

The coefficient matrix is:
[10.0, 1.0, 0.0, 2.5]
[1.0, 12.0, -0.3, 1.1]
[0.0, -0.3, 9.5, 0.0]
[2.5, 1.1, 0.0, 6.0]

The constant matrix is:
[2.2]
[2.85]
[2.79]
[2.87]


Solution using cholesky :
x_1 = 0.10
x_2 = 0.20
x_3 = 0.30
x_4 = 0.40

"""

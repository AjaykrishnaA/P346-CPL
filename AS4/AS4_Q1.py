from myLibrary import (getMatFromFile,
                       displayMat,
                       solve_LU, crout)

# augmented matrix:
Mat = getMatFromFile("q1mat")
vec = [6, -3, -2, 0]
b = [[vec[i]] for i in range(len(vec))]
print("\nThe coefficient matrix is:")
displayMat(Mat)
print("The constant matrix is:")
displayMat(b)
print("Solution using doolittle : ")
solve_LU(Mat, b, 4, "doolittle")
print("\nSolution using crout : ")
solve_LU(Mat, b, 4, "crout")
print("\n")

#################################### OUTPUT ####################################
""" 

The coefficient matrix is:
[1.0, 0.0, 1.0, 2.0]
[0.0, 1.0, -2.0, 0.0]
[1.0, 2.0, -1.0, 0.0]
[2.0, 1.0, 3.0, -2.0]

The constant matrix is:
[6.0]
[-3.0]
[-2.0]
[0.0]

Solution using doolittle :
x_1 = 1.0
x_2 = -1.0
x_3 = 1.0
x_4 = 2.0

Solution using crout :
x_1 = 1.0
x_2 = -1.0
x_3 = 1.0
x_4 = 2.0

"""

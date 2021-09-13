from myLibrary import (getMatFromFile,
                       displayMat,
                       lu_Inverse)

# augmented matrix:
Mat = getMatFromFile("q2mat")

print("\nThe matrix for checking and hence finding inverse is:")
displayMat(Mat)
print("\nInverse of the matrix is:")
displayMat(lu_Inverse(Mat, 4))
#################################### OUTPUT ####################################
""" 
The matrix for checking and hence finding inverse is:
[0.0, 2.0, 8.0, 6.0]
[0.0, 0.0, 1.0, 2.0]
[0.0, 1.0, 0.0, 1.0]
[3.0, 7.0, 1.0, 0.0]


Inverse of the matrix is:
[-0.25, 1.67, -1.83, 0.33]
[0.08, -0.67, 0.83, 0.0]
[0.17, -0.33, -0.33, 0.0]
[-0.08, 0.67, 0.17, -0.0]
"""

# This program gets the matrices A,B,C,D from respective csv files and do some operations on them.
import csv


def getMatFromFile(mat_name: str):
    # opening the file to read its contents
    with open(f'{mat_name}.csv', newline='') as file:

        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')

        # storing all the rows in an output list
        output = []
        for row in reader:
            output.append(row[:])

    return output


def displayMat(mat):
    if mat:
        for rows in mat:
            print(rows)
    print()


def nrow(mat):
    return len(mat)  # returns the no. of rows of a matrix


def ncol(mat):
    return len(mat[0])  # returns the no. of columns of a matrix


def matTranspose(mat):
    return [[mat[j][i] for j in range(nrow(mat))] for i in range(ncol(mat))]


def matMult(matA, matB):
    if ncol(matA) == nrow(matB):
        return [[sum(matA[i][k]*matB[k][j] for k in range(ncol(matA)))
                 for j in range(ncol(matB))] for i in range(nrow(matA))]
    else:
        print("\nIndexes do not match for matrix multiplication of %s and %s!" % (
            str(matA), str(matB)))


def matDot(matA, matB):
    # Checking if both the vectors are either row or column vectors
    if (nrow(matA) == 1 or ncol(matA) == 1) and (nrow(matB) == 1 or ncol(matB) == 1):
        # Following checks will enable to take dot product regardless of whether the inputs are row or column vectors.
        if ncol(matA) == nrow(matB) != 1:
            return matMult(matA, matB)[0]
        elif ncol(matA) == ncol(matB) != 1:
            return matMult(matA, matTranspose(matB))[0]
        elif nrow(matA) == nrow(matB) != 1:
            return matMult(matTranspose(matA), matB)[0]
        elif nrow(matA) == ncol(matB) != 1:
            return matMult(matB, matA)[0]
        # seperate check if both are single column single row vectors
        elif ncol(matA) == nrow(matB) == nrow(matA) == ncol(matB) == 1:
            return matMult(matA, matB)[0]
        else:
            print("\nDot product can only be taken upon vectors with same dimension!")
    else:
        print("\nDot product can only be taken upon vectors!")


# Get the matrices from respective files :
mat_A = getMatFromFile("mat_A")
mat_B = getMatFromFile("mat_B")
mat_C = getMatFromFile("mat_C")
mat_D = getMatFromFile("mat_D")

""" var_holder = {}
 
for i in ["A", "B", "C", "D"]:
    var_holder['mat_' + str(i)] = getMatFromFile(f"mat_{i}")
 
locals().update(var_holder) """

# Display the matrices :
""" print()
print("The matrix A is :")
displayMat(mat_A)
print("The matrix B is :")
displayMat(mat_B)
print("The matrix C is :")
displayMat(mat_C)
print("The matrix D is :")
displayMat(mat_D)  """


for i in ["A", "B", "C", "D"]:
    print(f"The matrix {i} is :")
    displayMat(vars()[f'mat_{i}'])

# Display the results :
print("The dot product of matrices C and D is :")
displayMat(matDot(mat_C, mat_D))
print("The matrix AB is :")
displayMat(matMult(mat_A, mat_B))
print("The matrix CA is :")
displayMat(matMult(mat_C, mat_A))
print("The matrix BDᵀ is :")
displayMat(matMult(mat_B, matTranspose(mat_D)))


#################################### OUTPUT ####################################

"""

################# 1 ###################

The matrix A is :
[1.0, 0.0, 1.0]
[2.0, 0.0, 1.0]
[0.0, 2.0, 1.0]

The matrix B is :
[1.0, 0.0, 1.0]
[0.0, 0.5, 1.0]
[0.0, 1.0, 1.0]

The matrix C is :
[2.0, 1.0, 1.0]

The matrix D is :
[6.0, 6.0, 6.0]

The dot product of matrices C and D is :
24.0

The matrix AB is :
[1.0, 1.0, 2.0]
[2.0, 1.0, 3.0]
[0.0, 2.0, 3.0]

The matrix CA is :
[4.0, 2.0, 4.0]

The matrix BDᵀ is :
[12.0]
[9.0]
[12.0]

################# 2 ###################

The matrix A is :
[9.0, 0.0, 6.0]
[2.0, 4.0, 7.0]
[3.0, 2.0, 1.0]

The matrix B is :
[1.0, 0.0, 6.0]
[3.0, 0.5, 8.0]
[5.0, 1.0, 2.0]

The matrix C is :
[2.0, 3.0, 9.0]

The matrix D is :
[3.0, 4.0, 2.0]

The dot product of matrices C and D is :
36.0

The matrix AB is :
[39.0, 6.0, 66.0]
[49.0, 9.0, 58.0]
[14.0, 2.0, 36.0]

The matrix CA is :
[51.0, 30.0, 42.0]

The matrix BDᵀ is :
[15.0]
[27.0]
[23.0]

################# 3 ###################

The matrix A is :
[8.0, 0.0, 3.0]
[2.0, 0.0, 4.0]
[4.0, 1.0, 1.0]

The matrix B is :
[3.0, 0.5, 8.0]
[5.0, 1.0, 2.0]
[3.0, 2.0, 1.0]

The matrix C is :
[2.0, 3.0, 4.0]

The matrix D is :
[3.0, 10.0, 2.0]

The dot product of matrices C and D is :
44.0

The matrix AB is :
[33.0, 10.0, 67.0]
[18.0, 9.0, 20.0]
[20.0, 5.0, 35.0]

The matrix CA is :
[38.0, 4.0, 22.0]

The matrix BDᵀ is :
[30.0]
[29.0]
[31.0]

################# 4 ###################

The matrix A is :
[9.0, 0.0]
[2.0, 4.0]
[3.0, 2.0]

The matrix B is :
[1.0, 0.0, 6.0]
[3.0, 0.5, 8.0]
[5.0, 1.0, 2.0]

The matrix C is :
[2.0, 3.0, 9.0, 4.0]

The matrix D is :
[3.0, 4.0, 2.0]

The dot product of matrices C and D is :

Dot product can only be taken upon vectors with same dimension!

The matrix AB is :

Indexes do not match for matrix multiplication of [[9.0, 0.0], [2.0, 4.0], [3.0, 2.0]] and [[1.0, 0.0, 6.0], [3.0, 0.5, 8.0], [5.0, 1.0, 2.0]]!

The matrix CA is :

Indexes do not match for matrix multiplication of [[2.0, 3.0, 9.0, 4.0]] and [[9.0, 0.0], [2.0, 4.0], [3.0, 2.0]]!

The matrix BDᵀ is :
[15.0]
[27.0]
[23.0]

################# 5 ###################

The matrix A is :
[9.0, 0.0, 6.0, 3.0]
[2.0, 4.0, 7.0, 3.0]
[3.0, 2.0, 1.0, 2.0]
[5.0, 3.0, 8.0, 4.0]

The matrix B is :
[1.0, 0.0, 6.0]
[3.0, 0.5, 8.0]
[5.0, 1.0, 2.0]
[3.0, 2.0, 1.0]

The matrix C is :
[2.0, 3.0]
[9.0, 4.0]

The matrix D is :
[3.0, 4.0, 2.0]

The dot product of matrices C and D is :

Dot product can only be taken upon vectors!

The matrix AB is :
[48.0, 12.0, 69.0]
[58.0, 15.0, 61.0]
[20.0, 6.0, 38.0]
[66.0, 17.5, 74.0]

The matrix CA is :

Indexes do not match for matrix multiplication of [[2.0, 3.0], [9.0, 4.0]] and [[9.0, 0.0, 6.0, 3.0], [2.0, 4.0, 7.0, 3.0], [3.0, 2.0, 1.0, 2.0], [5.0, 3.0, 8.0, 4.0]]!

The matrix BDᵀ is :
[15.0]
[27.0]
[23.0]
[19.0]

"""

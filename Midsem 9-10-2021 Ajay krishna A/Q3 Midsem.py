import math
import myLibrary as Lib
#AjaykrishnaA 1911017
Mat = Lib.getMatFromFile("Q3mat")
vec = [-9, 5, 7, 11]
b = [[vec[i]] for i in range(len(vec))]
print("\nThe coefficient matrix is:")
Lib.displayMat(Mat)
print("The constant matrix is:")
Lib.displayMat(b)
print("Solution using doolittle : ")
x = Lib.solve_LU(Mat, b, 4, "doolittle")


print("\nChecking the solution...\n")
#AjaykrishnaA 1911017
if sum([x[0]*(-9), x[1]*5, x[2]*(-5), x[3]*(12)]) == 11:
    print("The last equation is verified. Hence the solution is correct.")
else:
    print("The solution is wrong!")

#################################### OUTPUT ####################################
""" 
#AjaykrishnaA 1911017
The coefficient matrix is:
[3.0, -7.0, -2.0, 2.0]
[-3.0, 5.0, 1.0, 0.0]
[6.0, -4.0, 0.0, -5.0]
[-9.0, 5.0, -5.0, 12.0]

The constant matrix is:
[-9.0]
[5.0]
[7.0]
[11.0]

Solution using doolittle :
x_1 = 3.00
x_2 = 4.00
x_3 = -6.00
x_4 = -1.00

Checking the solution...

The last equation is verified. Hence the solution is correct.

"""

# This is interactive program.

initial_comment = "This program takes an integer N>=2 as an input and outputs the average distance between two points in a straight line made of discrete points in the range (2,N)."
later_comment = "Try once more?"
current_comment = initial_comment

# Repeat the code 7 times for easy checking:
for k in range(7):
    print()
    print(current_comment)
    # Taking input from user
    # Empty input will attach "9" to the input
    num = input("Type an integer greater than or equal to 2 : ") or "9"
    print()
    if num.isnumeric() and int(num) >= 2:
        N = int(num)
        for l in range(2, N+1):
            a = 0
            for i in range(1, l+1):
                for j in range(1, l+1):
                    a += abs(i-j)/l**2
            print(l, "     ", format(a, '.6f'))
    else:
        print("Invalid input! Try again with an integer greater than 1.")
    current_comment = later_comment
# end of for loop


###################################################### OUTPUT ######################################################

"""

This program takes an integer N>=2 as an input and outputs the average distance between two points in a straight line made of discrete points in the range (2,N).
Type an integer greater than or equal to 2 : 2

2       0.500000

Try once more?
Type an integer greater than or equal to 2 : 9

2       0.500000
3       0.888889
4       1.250000
5       1.600000
6       1.944444
7       2.285714
8       2.625000
9       2.962963

Try once more?
Type an integer greater than or equal to 2 : 25

2       0.500000
3       0.888889
4       1.250000
5       1.600000
6       1.944444
7       2.285714
8       2.625000
9       2.962963
10       3.300000
11       3.636364
12       3.972222
13       4.307692
14       4.642857
15       4.977778
16       5.312500
17       5.647059
18       5.981481
19       6.315789
20       6.650000
21       6.984127
22       7.318182
23       7.652174
24       7.986111
25       8.320000

Try once more?
Type an integer greater than or equal to 2 : 0

Invalid input! Try again with an integer greater than 1.

Try once more?
Type an integer greater than or equal to 2 : -40

Invalid input! Try again with an integer greater than 1.

Try once more?
Type an integer greater than or equal to 2 : v 

Invalid input! Try again with an integer greater than 1.

"""

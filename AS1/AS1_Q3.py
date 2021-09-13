# This is an interactive program.
initial_comment = "This program gives the factorial of the number input by you."
later_comment = "Try once more?"
current_comment = initial_comment


def my_factorial(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact


for i in range(7):
    print(current_comment)
    # Taking input from user
    # Empty input will attach "5" to the input
    input_num = input("Type a number: ") or "5"
    if input_num.isnumeric():
        n = int(input_num)
        print("The number", n, "factorial is:", my_factorial(n))
    else:
        print("Type a counting number!")
    current_comment = later_comment
# end of for loop


#################################### OUTPUT ####################################

"""

This program gives the factorial of the number input by you.
Type a number: 2
The number 2 factorial is: 2
Try once more?
Type a number: 3
The number 3 factorial is: 6
Try once more?
Type a number: 4
The number 4 factorial is: 24
Try once more?
Type a number: 5
The number 5 factorial is: 120
Try once more?
Type a number: 0
The number 0 factorial is: 1
Try once more?
Type a number: -5
Type a counting number!

"""
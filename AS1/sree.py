# This program finds the sum of first n terms of an HP
# First we need to take the number of term as input
number = input("please type the number of terms: ") or "1"
# we need to take the first term as input
first_term = float(input("please enter the first term of the HP: "))
# set the common difference
common_difference = 1.5
flag = 1
# We need to check whether the input given is a natural number
if number.isnumeric():
    k = float(first_term)
    n = int(number)
    # check whether the number is too large to process
    if n < 10000000:
        # using flag to check whether the HP contains an indeterminate number
        for i in range(n):
            if float(first_term**(-1))+i*common_difference == 0:
                flag = 0
        # when all the terms are in detrminate form will calculate the summ
        if flag == 1:
            for j in range(n-1):
                k = k+((float(first_term)**(-1)+j*common_difference)**(-1))
            print("The sum of the HP is : ", k)
        # if a term is in indeterminate form display a message stating so
        else:
            print("one of the term is in indeterminate form, please try another HP")
    else:
        # if the number is too big, asking the user to continue or not
        print("the number of terms is too large and may take time to process")
        confirmation = input(
            "Are you sure you want to continue?, please type yes or no: ")
        if confirmation == "yes":
            # if the answer is yes, will calculate the sum
            for i in range(1, n):
                k = k+(float(first_term)+i*common_difference)**(-1)
            print("The sum of the HP is: ", k)
        # if the user inputs no, then the program is terminated and needs to run again for another number
        elif confirmation == "no":
            print("please start again with a smaller number")
        # if the user inputs something other than yes/no, a message is given for invalid input
        else:
            print("the input given is invalid")
# If the number of terms given was not a natural number, the program is terminated with a message stating so
else:
    print("The number of terms given is not a natural number, please enter a natural number")

######################## output ################################
"""
please type the number of terms: 56
please enter the first term of the HP: 2
The sum of the HP is :  4.76961213858227

please type the number of terms: 47
please enter the first term of the HP: 2.5
The sum of the HP is :  4.947960381261763

please type the number of terms: 87
please enter the first term of the HP: 1.2
The sum of the HP is :  4.815229172826617

please type the number of terms: 9
please enter the first term of the HP: -3
one of the term is in indeterminate form, please try another HP

please type the number of terms: 5000000000
please enter the first term of the HP: 56
the number of terms is too large and may take time to process
Are you sure you want to continue?, please type yes or no: no
please start again with a smaller number
"""

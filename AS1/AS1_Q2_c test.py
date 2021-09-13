# This is an interactive program.
s = 0
initial_comment = "This program gives the sum of first 'n' terms of a Harmonic Progression(HP); 'n', 'first term' given by your input and common difference (of the corresponding AP) defaulted to 1.5. Input the first term and then a number."
later_comment = "Try once more?"
current_comment = initial_comment

for i in range(7):
    print(current_comment)
    # Taking input from user
    # Empty input will attach "1" to the input
    first_term = input("Type the first term: ") or "1"
    # Empty input will attach "3" to the input
    input_num = input("Type a number: ") or "3"
    com_diff = 1.5
    if input_num.isnumeric():
        n = int(input_num)
        a = float(first_term)
        # iteration to find the sum
        flag = 0
        for i in range(n):
            if a == 0:
                flag = 1
                break
            a_n_AP = (a**(-1) + i*com_diff)  # n_th term of corr. AP
            if a_n_AP == 0:
                flag = 1
                break
            a_n = a_n_AP**(-1) # n_th term of HP
            s = s + a_n
        if flag == 0:
            print("Sum of first", n, "terms of the input HP ", a, ",",
                  (a**(-1) + com_diff)**(-1), ",", (a**(-1) + 2*com_diff)**(-1), ",... " "is:", s)
        else:
            print("The sum calculation requires division by zero! Please try again using a different input.")

    else:
        print("Type a counting number!")
    s = 0
    current_comment = later_comment
# end of while loop


####################################################################### OUTPUT #######################################################################

# This program gives the sum of first 'n' terms of a Harmonic Progression(HP); 'n', 'first term' given by your input and common difference (of the corresponding AP) defaulted to 1.5. Input the first term and then a number.
# Type the first term: 1
# Type a number: 1
# Sum of first 1 terms of the input HP  1.0 , 0.4 , 0.25 ,... is: 1.0
# Try once more?
# Type the first term: .5
# Type a number: 3
# Sum of first 3 terms of the input HP  0.5 , 0.2857142857142857 , 0.2 ,... is: 0.9857142857142858
# Try once more?
# Type the first term: .1
# Type a number: 4
# Sum of first 4 terms of the input HP  0.1 , 0.08695652173913043 , 0.07692307692307693 ,... is: 0.3328451159035867
# Try once more?
# Type the first term: 0
# Type a number: 3
# The sum calculation requires division by zero! Please try again using a different input.
# Try once more?
# Type the first term: -.666666666666666666666666666
# Type a number: 2
# The sum calculation requires division by zero! Please try again using a different input.

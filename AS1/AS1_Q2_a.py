# This is an interactive program.
s = 0
init_com = "This program gives the sum of first 'n' terms of an Arithmatic Progression(AP); 'n', 'first term' given by your input and common difference defaulted to 1.5. Input the first term and then a number."
later_com = "Try once more?"
cur_com = init_com

for i in range(7):
    print(cur_com)
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
        for i in range(n):
            a_n = a + i*com_diff #n_th term
            s = s + a_n
        print("Sum of first", n, "terms of the input AP ", a, ",",
              a+com_diff, ",", a+2*com_diff, ",... " "is:", s)

    else:
        print("Type a counting number!")
    s = 0
    cur_com = later_com
# end of while loop


############################## OUTPUT ##############################

# This program gives the sum of first 'n' terms of an Arithmatic Progression(AP), 'n', 'first term' given by your input and common difference defaulted to 1.5. Input the first term and then a number.
# Type the first term: 1
# Type a number: 1
# Sum of first 1 terms of the input AP  1 , 2.5 , 4.0 ,... is: 1.0
# Try once more?
# Type the first term: 1
# Type a number: 2
# Sum of first 2 terms of the input AP  1 , 2.5 , 4.0 ,... is: 3.5
# Try once more?
# Type the first term: 2
# Type a number: 3
# Sum of first 3 terms of the input AP  2 , 3.5 , 5.0 ,... is: 10.5
# Try once more?
# Type the first term: 0
# Type a number: 0
# Sum of first 0 terms of the input AP  0 , 1.5 , 3.0 ,... is: 0
# Try once more?
# Type the first term: -1
# Type a number: 3
# Sum of first 3 terms of the input AP  -1 , 0.5 , 2.0 ,... is: 1.5
# Try once more?
# Type the first term: 0
# Type a number: -1
# Type a counting number!

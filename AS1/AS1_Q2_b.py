# This is an interactive program.
s = 0
init_com = "This program gives the sum of first 'n' terms of a Geometric Progression(GP); 'n', 'first term' given by your input and common ratio defaulted to 0.5. Input the first term and then a number."
later_com = "Try once more?"
cur_com = init_com

for i in range(7):
    print(cur_com)
    # Taking input from user
    # Empty input will attach "1" to the input
    first_term = input("Type the first term: ") or "1"
    # Empty input will attach "3" to the input
    input_num = input("Type a number: ") or "3"
    com_ratio = 0.5
    if input_num.isnumeric():
        n = int(input_num)
        a = float(first_term)
        # iteration to find the sum
        for i in range(n):
            a_n = a*(com_ratio)**i  # n_th term
            s = s + a_n
        print("Sum of first", n, "terms of the input GP ", a, ",",
              a*(com_ratio), ",", a*(com_ratio)**2, ",... " "is:", s)

    else:
        print("Invalid input! Type a counting number.")
    s = 0
    cur_com = later_com
# end of while loop


############################## OUTPUT ##############################

# This program gives the sum of first 'n' terms of a Geometric Progression(GP); 'n', 'first term' given by your input and common ratio defaulted to 0.5. Input the first term and then a number.
# Type the first term: 1
# Type a number: 1
# Sum of first 1 terms of the input GP  1 , 0.5 , 0.25 ,... is: 1.0
# Try once more?
# Type the first term: 2
# Type a number: 3
# Sum of first 3 terms of the input GP  2 , 1.0 , 0.5 ,... is: 3.5
# Try once more?
# Type the first term: 4
# Type a number: 0
# Sum of first 0 terms of the input GP  4 , 2.0 , 1.0 ,... is: 0
# Try once more?
# Type the first term: 0
# Type a number: 3
# Sum of first 3 terms of the input GP  0 , 0.0 , 0.0 ,... is: 0.0
# Try once more?
# Type the first term: -8
# Type a number: 3
# Sum of first 3 terms of the input GP  -8 , -4.0 , -2.0 ,... is: -14.0
# Try once more?
# Type the first term: 2
# Type a number: a
# Invalid input! Type a counting number.

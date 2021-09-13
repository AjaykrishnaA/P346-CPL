# This is an interactive program.
s = 1
init_com = "This program gives the sum of first 'n' natural numbers, 'n' given by your input."
later_com = "Try once more?"
cur_com = init_com
for i in range(7):
    print(cur_com)
    # Taking input from user
    # Empty input will attach "5" to the input
    input_num = input("Type a number: ") or "5"
    if input_num.isnumeric():
        n = int(input_num)
        # iteration to find the sum
        if n >= 1:
            for i in range(1, n):
                s = s+i+1
            print("Sum of first", n, "natural numbers is:", s)
        else:
            print("Type a counting number!")
    else:
        print("Type a counting number!")
    s = 1
    cur_com = later_com
# end of while loop


#################################### OUTPUT ####################################

# This program gives the sum of first 'n' natural numbers, 'n' given by your input.
# Type a number: 3
# Sum of first 3 natural numbers is: 6
# Try once more?
# Type a number: 9
# Sum of first 9 natural numbers is: 45
# Try once more?
# Type a number: 0
# Type a counting number!
# Try once more?
# Type a number: -11
# Type a counting number!
# Try once more?
# Type a number: 1
# Sum of first 1 natural numbers is: 1

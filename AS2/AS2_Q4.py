# This is an interactive program.
from math import ceil
import random
comment = "The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!"


l = {"France": "Paris", "United States": "Washington", "Germany": "Berlin", "England": "London", "Canada": "Ottawa", "Australia": "Canberra", "Netherlands": "Amsterdam", "Japan": "Tokyo", "Sweden": "Stockholm", "Brazil": "Brasilia", "Spain": "Madrid", "Norway": "Oslo",
     "South Korea": "Seoul", "China": "Beijing", "Italy": "Rome", "New Zealand": "Wellington", "Scotland": "Edinburgh", "Thailand": "Bangkok", "Argentina": "BuenosAires", "Chile": "Santiago", "Nigeria": "Abuja", "Cameroon": "Yaounde", "South Africa": "CapeTown", "Jamaica": "Kingston"}

hint = False
hangShield = 30

for i in range(7):
    hint = False
    print("\n"+comment)
    hintChoice = input("Press 'Y' if you want hint : ")
    if hintChoice == 'Y':
        hint = True
    country, capital = random.choice(list(l.items()))
    if hint:
        print("\nHint :", country)
    capital_letters = list(capital)
    lives = ceil(hangShield*.01*len(capital_letters))

    progress = ["_" for i in capital_letters]

    flag = 0
    while lives != 0 and flag == 0:
        print("\nYour progress : ", " ".join(progress))
        print()
        print("Lives Remaining: ", lives)

        guess = input("Guess a letter : ")

        if guess.lower() in capital.lower():
            lives += 1
            for i in range(len(capital_letters)):
                if guess.lower() == capital_letters[i].lower():
                    progress[i] = capital_letters[i]
        lives -= 1
        if progress == capital_letters:
            print("\nCongratulations! You Won!!!\n")
            flag = 1
    if lives == 0:
        print("\nOh, you lost it! Go hang yourself. The capital was "+capital+"!\n")
    new_game = input("Try once more? Press 'Y'. Press anything else to exit:")
    if new_game != "Y":
        break
# end of for loop


#################################### OUTPUT ####################################

"""
################# 1 ###################

The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!
Press 'Y' if you want hint : n

Your progress :  _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : a

Your progress :  _ a _ _ _ _ _

Lives Remaining:  3
Guess a letter : c

Your progress :  _ a _ _ _ _ _

Lives Remaining:  2
Guess a letter : o

Your progress :  _ a _ _ _ o _

Lives Remaining:  2
Guess a letter : t

Your progress :  _ a _ _ _ o _

Lives Remaining:  1
Guess a letter : s

Oh, you lost it! Go hang yourself. The capital was Bangkok!

Try once more? Press 'Y'. Press anything else to exit:Y

################# 2 ###################

The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!
Press 'Y' if you want hint : Y

Hint : South Africa

Your progress :  _ _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : c

Your progress :  C _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : a

Your progress :  C a _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : p

Your progress :  C a p _ _ _ _ _

Lives Remaining:  3
Guess a letter : e

Your progress :  C a p e _ _ _ _

Lives Remaining:  3
Guess a letter : t

Your progress :  C a p e T _ _ _

Lives Remaining:  3
Guess a letter : o

Your progress :  C a p e T o _ _

Lives Remaining:  3
Guess a letter : w

Your progress :  C a p e T o w _

Lives Remaining:  3
Guess a letter : n

Congratulations! You Won!!!

################# 3 ###################

The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!
Press 'Y' if you want hint : Y

Hint : China

Your progress :  _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : b

Your progress :  B _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : e

Your progress :  B e _ _ _ _ _

Lives Remaining:  3
Guess a letter : i

Your progress :  B e i _ i _ _

Lives Remaining:  3
Guess a letter : j

Your progress :  B e i j i _ _

Lives Remaining:  3
Guess a letter : n

Your progress :  B e i j i n _

Lives Remaining:  3
Guess a letter : g

Congratulations! You Won!!!

Try once more? Press 'Y'. Press anything else to exit:Y

################# 4 ###################

The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!
Press 'Y' if you want hint : n

Your progress :  _ _ _ _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : a

Your progress :  _ a _ _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : c

Your progress :  _ a _ _ _ _ _ _ _ _

Lives Remaining:  2
Guess a letter : o

Your progress :  _ a _ _ _ _ _ _ o _

Lives Remaining:  2
Guess a letter : i

Your progress :  _ a _ _ i _ _ _ o _

Lives Remaining:  2
Guess a letter : s

Your progress :  _ a s _ i _ _ _ o _

Lives Remaining:  2
Guess a letter : w

Your progress :  W a s _ i _ _ _ o _

Lives Remaining:  2
Guess a letter : h

Your progress :  W a s h i _ _ _ o _

Lives Remaining:  2
Guess a letter : n

Your progress :  W a s h i n _ _ o n

Lives Remaining:  2
Guess a letter : t

Your progress :  W a s h i n _ t o n

Lives Remaining:  2
Guess a letter : g

Congratulations! You Won!!!

Try once more? Press 'Y'. Press anything else to exit:

################# 5 ###################

The mischevious Hangman game is back. Try your best not to hang yourself by guessing the country's capital right!
Press 'Y' if you want hint : n

Your progress :  _ _ _ _ _ _ _

Lives Remaining:  3
Guess a letter : a

Your progress :  _ _ _ _ _ _ _

Lives Remaining:  2
Guess a letter : o

Your progress :  _ _ _ _ _ _ _

Lives Remaining:  1
Guess a letter : e

Your progress :  _ e _ _ _ _ _

Lives Remaining:  1
Guess a letter : s

Oh, you lost it! Go hang yourself. The capital was Beijing!

Try once more? Press 'Y'. Press anything else to exit:
"""

# """
# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Michaela Sebakova
# email: michaela.sebakova@seznam.cz
# """

import random
separator = "-----------------------------------------------"

# define introduction
intro_text = """
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
----------------------------------------------- """

# user guess and its conditions
# Request the number until pass the validations
def user_guess():
    validNumber = True
    print()
    guess = input(f"Enter a number:\n{separator}\n")
    # numbers only
    if not guess.isdigit():
        print ("You can insert numbers only!")
        validNumber = False
    # 4 characters only
    elif (len(guess) != 4):
        print("Your guess must be 4 characters long!")
        validNumber = False
    # cannot start with 0
    elif int(guess[0]) ==0:
        print("Your number cannot start with 0!")
        validNumber = False
    # no duplicate value
    for i in guess:
        if guess.count(i) != 1:
            print("You cannot insert duplicates!")
            validNumber = False
    
    if validNumber == False:
        return user_guess()

    return guess

# get the secret number and check there is no duplicate number
def secret_number():
    number = random.randint(1000,9999)
    for i in str(number):
        if str(number).count(i) != 1:
            number = random.randint(1000,9999)
        else:
            pass

    return number

def bulls_cows(number,guess):
    bulls = 0
    digitsBulls = []
    cows = 0
    digitsCows = []
    for i in range(4):
        if number[i] == guess[i]:
            bulls +=1
            digitsBulls.append(number[i])
    for i in range(4):
        for j in range(4):
            if number[i] == guess[j] and (guess[j] not in digitsBulls):
                cows +=1
                digitsCows.append(number[i])

    if bulls > 0:
        print('Bulls: {0} ({1})'.format(bulls, ' and '.join(digitsBulls)))
    if cows > 0:
        print('Cows: {0} ({1})'.format(cows, ' and '.join(digitsCows)))


secretNumber = secret_number()
#print(secretNumber) #Enable this line if you want to se the secret number
print(intro_text)
userGuessNumber = False
while (userGuessNumber == False):
    validNumber = user_guess()
    bulls_cows(secretNumber, validNumber)
    if validNumber == secretNumber:
        print ("Correct, you've guessed the right number")
        userGuessNumber = True



#Guess My Number

import random

# In this commented out region we tweaked the ask_number function
# so that it would return an error message if the users input is
# outside of the range

##def ask_number(question, low, high):
##    response = int(raw_input(question))
##    while response not in range(low, high):
##        print "ERROR: Number outside of range (",low,"-", high,")"
##        response = int(raw_input(question))
##    return response

# Define a function that asks a user for an integer untill they enter
# one.

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response


# Print information about the game.

print "\tWelcome to 'Guess My Number'!"
print "\nI'm thinking of a number between 1 and 100."
print "Try to guess it in as few attempts as possible.\n"

#set the initial values

the_number = random.randrange(100)+1
guess = ask_number("Take a guess: ", 1, 100)
tries = 1

#guessing loop

while (guess != the_number):
    if (guess > the_number):
        print "Lower..."
    else:
        print "Higher..."

    guess = ask_number("Take a guess: ", 1, 100)
    tries += 1

# Tell the user they guessed the correct number.

print "You guessed it! The number was", the_number
print "And it only took you",tries,"tries!\n"

# Exit the program

raw_input("\n\nPress the enter key to exit.")

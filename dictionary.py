

#Word Jumble

#The computer picks a random word and then "jumbles" it
#The player has to guess the original word

import random


# Define a function that prints the game's instructions

def instructions():
    instruct = \
"""
    Welcome to Word Jumble!

    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
    print instruct


# Define a function that picks a random word out of a list of keys
# in a dictionary.

def random_word():
    WORDS = {"python":"p", "jumble":"j", "easy":"e",
         "difficult":"d", "answer":"a", "xylophone":"x"}

    words = WORDS.keys()
    word = random.choice(words)

    return word

# Define a function that takes a string as an input, and returns a string
# containing the same letters as in the input string, but in a different order

def jumble(word):
    jumble = ""

    start_word = word

    while start_word:
        position = random.randrange(len(start_word))
        jumble += start_word[position]
        start_word = start_word[:position] + start_word[(position + 1):]

    return jumble

# Define a function that plays the jumble game.

def play(word,jumble):

    WORDS = {"python":"p", "jumble":"j", "easy":"e",
         "difficult":"d", "answer":"a", "xylophone":"x"}
    
    print "The jumble is:", jumble

# Ask the user to guess what the jumbled word is

    guess = raw_input("\nYour guess: ")
    guess = guess.lower()

# While their guess is not correct, if they input hint provide them with
# a hint, otherwise tell them they are wrong. Ask them to guess again

    while guess != word and guess != "":

        if guess == "hint":
            print "The word begins with", WORDS[word]
            guess = raw_input("Guess again: ")

        else:        
            print "Sorry, that's not it."
            guess = raw_input("Your guess: ")
            guess = guess.lower()

# If their guess is correct tell them

    print "That's it! You guessed it!\n"
    print "Thanks for playing"
    raw_input("\n\nPress the enter key to exit.")
    
# Define and call a main function that uses the previously defined functions
# to play the game.

def main():
    instructions()
    the_word = random_word()
    the_jumble = jumble(the_word)
    play(the_word,the_jumble)

main()
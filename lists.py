import random

# David Rodgers
# INFO-I 210

# Define functions that contain nouns, verbs, and abjective in lists.
# Each function should return an item from its list when called.

def random_noun():
    nouns = ["Carrot People","Zombie Fat Albert","potato salad","Nick Cage","Steve Buscemi"]
    return nouns[random.randrange(5)]

def random_verb():
    verbs = ["smooth talked","twerked with","anticipated confrontation with","fell for","halved"]
    return verbs[random.randrange(5)]

def random_adjective():
    adjectives = ["spastic","gigantic","standard","fierce","unexpected"]
    return adjectives[random.randrange(5)]

# Define a function that generates a random sentace using the previously
# defined functions.

def random_sentance():
    return "The "+random_adjective()+" "+random_noun()+" "+random_verb()+" the "+random_adjective()+" "+random_noun()+". "

# Define a function that takes a number as an input, and outputs a string
# containing the specified number of sentances.

def random_essay(number):
    num = number
    output_str = ""
    while num > 0:
        output_str += random_sentance()
        num = num-1
    return output_str

# Ask the user how many sentances they want in a paragraph and print it.

number = int(raw_input("How many sentances would you like in your essay? "))
print "\nHere's your automatically-generated essay:\n"
print random_essay(number)
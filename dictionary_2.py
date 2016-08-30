#David Rodgers
#Individual Homework 5

print "This program allows the user to input a word which will be"
print "encoded within a message. The secret message will be printed"
print "back to the user.\n"


# Create a dictionary which holds the letters of the alphabet as keys
# and a word starting with the corresponding letter as the definitions. 

secret_dict = {"a" : "Apple", "b" : "Boat","c" : "Cat", "d" : "Dog", "e" : "Egg",
               "f" : "Far", "g" : "Goat", "h" : "House", "i" : "Ice", "j" : "Juice",
               "k" : "Kungfu", "l" : "Leg", "m" : "Mouse", "n" : "New", "o" : "Orange",
               "p" : "Place", "q" : "Quit", "r" : "Remove", "s" : "Star", "t" : "Time",
               "u" : "Up", "v" : "Vowel", "w" : "Water", "x" : "Xylophone", "y" : "You",
               "z" : "Zoo"}
print "----\n"

# Ask the user for a word to hide.

word = raw_input("What word should I hide? ")

output_string = ""

# Start a for loop which concatenates the definition of each letter in the
# users word onto the output string.

for letter in word:
    hidden = secret_dict.get(letter.lower())
    output_string += hidden+" "

# Print the output string

print "\n",output_string
print "\n----"
print "\nNow, let's make it a little more 'hidden' by reversing their order!"
print "\n----\n"

# Ask the user for another word to hide, this time in reverse.

reverse_word = raw_input("What word should I hide in reverse? ")

back_word = []

# Use a for loop to assign every character in the users word as a value
# in a list.

for char in reverse_word:
    back_word.append(char.lower())

# Reverse the order of the list.

back_word.reverse()

back_string = ""

# Start a for loop which concatenates the definition of each character in the
# list onto an output string.

for char in back_word:
    back_hidden = secret_dict.get(char)
    back_string += back_hidden+" "

# Print the output string.

print "\n",back_string
print "\n----"
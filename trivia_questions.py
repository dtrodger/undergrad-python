#Group Homework 7


#Trivia Challenge
#Trivia game that reads a plain text file

#display different trivia question options

import os

file_lists = os.listdir(os.getcwd())

trivia_files = []

for i in file_lists:
    if "trv" in i:
        trivia_files.append(i)

print "Your trivia options are ", trivia_files

chosen_game = raw_input("Please enter a filename: ")

#open the .txt file with the trivia questions

def open_file(file_name, mode):
    """Open a file"""
    while True:
        try:
            the_file = open(file_name, mode)
        except(IOError), e:
            print "Unable to open the file", file_name, "Ending program./n",e
            raw_input("\n\nPress enter key to exit.")
            sys.exit()
        else:
            return the_file

#pull the next file from a .txt file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

#pull a multiple lines from a .txt file

def next_block1(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answer = []
    for i in range(4):
        answer.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    point = next_line(the_file)

    return category, question, answer, correct, explanation, point

#welcome the user to the game

def welcome(title):
    """Welcome the player to get his/her name"""
    print "\t\tWelcome to the Trivia Challenge!\n"
    print "\t\t",title,"\n"

#run the game

def main():
    trivia_file = open_file(chosen_game, "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    #define next block
    category, question, answers, correct, explanation, point_value = next_block1(trivia_file)
    while category:
        #ask a question
        print "Category: ",category
        print "Question: ",question

        for i in range(4):
            print "\t", i + 1, "-", answers[i]
        #get answer
        answer = raw_input("What's your answer?: ")
        #check answer
        if answer == correct:
            print "\nRight!"
            score += int(point_value)
        else:
            print "\nWrong.",
            print explanation
        print "Score:", score, "\n\n"
    #get next block
        category, question, answers, correct, explanation, point_value = next_block1(trivia_file)
    trivia_file.close()
    print "That was the last question!"
    print "Your final score is:", score


main()
raw_input("\n\nPress the enter key to exit.")
#Trivia Challenge
#Trivia game that reads a plain text file




def open_file(file_name, mode):
    """Open a file"""
    try:
        the_file = open(file_name, mode)
    except(IOError), e:
        print "Unable to open the file", file_name, "Ending program./n",e
        raw_input("\n\nPress enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
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

def welcome(title):
    """Welcome the player to get his/her name"""
    print "\t\tWelcome to the Trivia Challenge!\n"
    print "\t\t",title,"\n"

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    category, question, answer, correct, explanation, point = next_block(trivia_file)
    while category:
        print category
        print question
        for i in range(4):
            print "\t", i + 1, "-", answer[i]

        answer = raw_input("What's your answer?: ")

        if answer == correct:
            print "\nRight!",
            score += int(point)
        else:
            print "\nWrong.",
        print explanation
        print "Score:", score, "\n\n"

        category, question, answer, correct, explanation, point = next_block(trivia_file)

    trivia_file.close()

    print "That was the last question!"
    print"Your final score is: ", score

        
main()
raw_input("\n\nPress the enter key to exit.")
        
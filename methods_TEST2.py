# Daivd Rodgers
# Practical 2

# Allows me to call functions from tools.py

from tools import *

# Define a function that pulls strings from each line in a .txt file and
# returns a table with the string information.

def print_course():

# Open the course_list file. Add the string values of each line to a variable
# using the readlines() opperation. Close the file.
    
    courses = open("course_list.txt", "r")

    course_ls = courses.readlines()

    courses.close()

# Strip and split each element in the course_ls, then append it to a new list.
# This creates a list that can be used as an input into the table print function

    final_ls = []

    for element in course_ls:
        new_el = element.strip().split()
        final_ls.append(new_el)

# Return the table print fuction with specified headers and the new list as the
# input.


    return table_print(["COURSE","SEM","CRED","GRADE"],final_ls)



# Define a function that allows the user to append text to an existing
# text file.

def add_course():
    y_n = raw_input("Would you like to add a course?(Y/N) ").upper()

# While the user wants to add another course...

    while y_n == "Y":

# First ask for the course information then concatenate the info into one
# string in the proper format.
        
        abb = raw_input("Please enter the course abbreviation: ").upper()
        semester = raw_input("Please enter the semester: ").upper()
        credit = raw_input("Please enter the number of credits: ")
        grade = raw_input("Please enter the grade: ").upper()

        new_row = "\n"+abb+"\t"+semester+"\t"+credit+"\t"+grade

# Open the course_list, append the new_row string, and close course_list.
        
        course_file = open("course_list.txt", "a")

        course_file.write(new_row)

        course_file.close()

# Tell the user the course has been added, print the new course table, and
# ask them if they want to add another course. If they enter N when asked
# about adding another course break out of the while loop (Specified when
# I call the while loop).

        print "Course added to course_list.txt"

        print_course()

        y_n = raw_input("Would you like to add a course?(Y/N) ").upper()

# Define a function that will return the sum of the credit hours in the
# course_list file.

def credit_print():

# Open the course_list file and use readlines() to add the string values of
# each of its lines to a variable. Close the course_list file
    
    credit_txt_file = open("course_list.txt", "r")

    credit_raw_ls = credit_txt_file.readlines()

    credit_txt_file.close()

# Strip and split every element in the credit_raw_ls, then add the 3rd index
# of the list to a new list (The third element, of index 2, is the credit
# hours in each class).

    credit_ls = []

    for element in credit_raw_ls:
        new_el = element.strip().split()
        credit_ls.append(new_el[2])

# Add the value of each of the elements in the new list together and output
# the result within a string specifying what the information means.

    total_credits = 0

    for num in credit_ls:
        int_num = int(num)
        total_credits += int_num

    str_credit_total = str(total_credits)


    return "Total credit hours: "+str_credit_total


# Call the functions defined above

print_course()
add_course()
print credit_print()
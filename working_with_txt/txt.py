#David Rodgers


import os, datetime

#takes one argument as a string. returns portion of string up to first vowel
def pl_prefix(string):
    output = ""
    
    for char in string:
        if char not in "aeiouy":
            output += char
        else:
            break

    return output
#takes one argument as a string. returns it withthe prefix and stem reversed at
#the vowel
def pl_reverse(string):
    pre = pl_prefix(string)

    stem = string.strip(pre)

    return stem+pre

#takes one arguement as a string. returns it translated into pig latin
def pl_translate(string):

    title = 0
    if string.istitle():
        title = 1

    if string[0].lower() in "aeiouy":
        if string[len(string)-1] in ",.:;":
            punc = string[len(string)-1]
            string = string.strip(punc)
            return string+"yay"+punc
        else:
            return string+"yay"
            
    elif string[len(string)-1] in ",.:;":
        punc = string[len(string)-1]
        string = string.strip(punc)
        string = pl_reverse(string)
        if title == 1:
            return string.capitalize()+"ay"+punc
        else:
            return string+"ay"+punc

    else:
        string = pl_reverse(string)
        if title == 1:
            return string.capitalize()+"ay"
        else:
            return string+"ay"
#reads text from a file. translates the text into pig latin then returns it
#into a new file.
def pig_file_create():
    input_file = raw_input("\nPlease enter a file name to be translated: ")

    while True:
        try:
            file_open = open(input_file, "r")
        except:
            print "EXCEPTION ERROR"
            input_file = raw_input("Please enter a file name: ")
        else:
            break
    read_file = file_open.read().split()
    file_open.close()

    now_date = datetime.date.today()
    now_time = datetime.datetime.today().time()
    output_txt = "Created on "+str(now_date)+" at "+str(now_time)+"\n\n"
    translated = " ".join([pl_translate(word) for word in read_file])
    output_txt += translated
    output_txt += "\n\nThank you for using the Pig Latin Translator."

    home = os.getcwd()
    path = home+"\\translations"
    os.chdir(path)

    output_file = input_file[:-4]
    output_file+="(pig).txt"
    
    trans_file = open(output_file, "w")
    trans_file.write(output_txt)
    trans_file.close()
    
print ".txt files in current directory:"
print "-"*32

dir_files = os.listdir(os.getcwd())

for a_file in dir_files:
    if ".txt" in a_file:
        print a_file

#run the pig file create function
pig_file_create()

            
        
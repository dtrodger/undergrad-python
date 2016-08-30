#David Rodgers
#I211 Practical 1



#put names from a text file into a list. sort the list.
suspects = [name for name in open("names.txt", "r").read().strip().split()]

suspects.sort()


#define a funciton that will print names in a list
def current_suspects(suspect_list):

#print a message specific the the number of names in the list
    if len(suspect_list) != 1:
        suspects = "Current Suspects:\n"
    else:
        suspects = "Killer Found!\n"
        
    suspects += "------------\n"

#start a count of names in the list
    suspect_count = 0

#for each name in the list add the name to the output string and
#add one to the count
    for name in suspect_list:
        suspects += name+" "
        suspect_count += 1

#add the count to the output string
    suspects += "\n("+str(suspect_count)+" possible)\n"

    return suspects


#use the currrent_suspects function to print the names from the text file
suspects_no_clue = current_suspects(suspects)

print suspects_no_clue





print "*** Clue 1: The killer's name is no more than 6 letters long ***\n"

#create a list containing suspects whose name is 6 characters or less
suspects_clue_1 = [name for name in suspects if len(name) <=6]

#put the new list through th current suspects funciton and print it
suspects_clue_1_str = current_suspects(suspects_clue_1)

print suspects_clue_1_str





print "*** Clue 2: The killer's name doesnt end in a vowel or start with 'D' ***\n"

#create a list of suspects whose names dont end in a vowel or start with D
suspects_clue_2 = [namee for namee in\
                   [name for name in suspects_clue_1 if name[len(name) - 1] not in "AEIOU"]\
                   if namee[0] != "D"]

#put the new list through th current suspects funciton and print it
suspects_clue_2_str = current_suspects(suspects_clue_2)

print suspects_clue_2_str





print "*** Clue 3: The killer's name has two vowels in it that are not 'O' ***\n"

#create a list of suspects whose names have two vowels that are not O
suspects_clue_3 = [name for name in suspects_clue_2\
                  if len([let for let in name if let in "AEIU"]) == 2]

#put the new list through th current suspects funciton and print it
suspects_clue_3_str = current_suspects(suspects_clue_3)

print suspects_clue_3_str





print "*** Clue 4: The killer's name has the same letter in it twice ***\n"

suspects_clue_4 = []

#create a list of suspects whose name has the same letter twice
for name in suspects_clue_3:
    for let in name:
        if name.count(let) == 2:
            suspects_clue_4.append(name)
            break
        
#put the new list through th current suspects funciton and print it
suspects_clue_4_str = current_suspects(suspects_clue_4)

print suspects_clue_4_str





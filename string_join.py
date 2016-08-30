#David Rodgers



#build a string containing worlds and numbers
message = "Hello 34215 World 5620 From 384 Bloomington"

#split the message at spaces, check is the split isalpha, if so append it
#to the list
#split the message at spaces. check if the split isdigit. if so append it
#to the list
#print the two lists using join
print " ".join([word for word in message.split(" ")\
       if word.isalpha()]) + " | ", "".join(sorted([num for num in message\
        if num.isdigit()]))
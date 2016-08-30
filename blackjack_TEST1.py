import random

#David Rodges
#Lab Practical 1
#Blackjack

#Create a variable containing an empty tuple to assign card values to.
#Create a variable that equals 0 to keep track of how many cards were
#put into initial hand.
#Create a variable that equals 0 to keep track of the total.

cur_hand = ()

start_hand_count = 0

score = 0

#While the count is less than 2 add a random number 1-10 as a new element
#to the current hand tuple. Also, add 1 to the count each time so the
#while loop breaks when the hand contains two values.

while start_hand_count < 2:
    num = random.randrange(1,10)
    num_tup = (num,)
    cur_hand += num_tup
    start_hand_count += 1

#Compute the value in their hand by using a for loop that adds the value
#of each element in the current hand tuple to the score variable.

for value in cur_hand:
    score += value

#Print their current and and score.

print "Your current hand: ",cur_hand
print "Score: ",score,"\n"

#Start a while loop that continues until the score is > 16.
#Each time the while loop runs pick another random number
#between 1-10 add it to the current hand tuple, add its
#value to the score variable, and print the current hand and score.

while score < 16:
    print "You take another card!"
    num = random.randrange(1,10)
    num_tup = (num,)
    cur_hand += num_tup
    score += num

    print "Your current hand: ",cur_hand
    print "Score: ",score,"\n"

#If the final score is > 21 print a message telling the user they loose.
#Otherwise, print a message telling them they cannot take any more cards

if score > 21:
    print "\t\t-------YOU LOSE-------"

else:
    print "You don't take any more cards!"
    



    
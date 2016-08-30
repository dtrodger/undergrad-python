import random

#create a class to build cars

class Car(object):

#the class needs a make and driver input, it assignes the cars miles to 0

    def __init__ (self, make, driver):
        self.miles = 0
        self.make = make
        self.driver = driver

#str incase the user wants to print the cars info

    def __str__ (self):
        reply = "Car object\n"
        reply += "Make: " + self.make + "\n"
        reply += "Mileage: " +str(self.miles) + "\n"
        return reply

#another method to print the cars info

    def info(self):
        print "This race car is a",make+"."
        print "This race car has", self.miles,"miles on it."

#when the car is driven a specific amount of miles is added to its milage.
#the miles varry by make and driver

    def drive(self):
        if self.driver == "Mario Andretti":
            if self.make == "BMW":
                self.miles += 50
            elif self.make == "Porsche":
                ran1 = random.randrange(30,70)
                ran2 = random.randrange(30,70)
                if ran1 > ran2:
                    self.miles += ran1
                else:
                    self.miles += ran2
            else:
                ran1 = random.randrange(10,90)
                ran2 = random.randrange(10,90)
                if ran1 > ran2:
                    self.miles += ran1
                else:
                    self.miles += ran2
        else:
            if self.make == "BMW":
                self.miles += 60
            elif self.make == "Porsche":
                ran1 = random.randrange(30,70)
                ran1 += 10
                self.miles += ran1
            else:
                ran1 = random.randrange(10,90)
                ran1 += 10
                self.miles += ran1
            
        

print \
      """
Welcome to the race!
--------------------------------------------------------
Each player, please select your care and driver.
Cars are BMW, Porsche, and Ferrari
Drivers are Mario Andretti and Tony Stewart
"""

#ask both players to enter their desired make and driver. if their entry is
#invalid tell them and ask them to enter again

p1_make = raw_input("Player 1, please enter your car: ")

while p1_make != "BMW" and p1_make != "Porsche" and p1_make != "Ferrari":
    p1_make = raw_input("Invalid entry choose either BMW, Porsche, or Ferrari: ")

p1_driver = raw_input("Player 1, please eter your driver: ")

while p1_driver != "Mario Andretti" and p1_driver != "Tony Stewart":
    p1_driver = raw_input("Invalid entry choose either Mario Andretti or Tony Stewart: ")


p2_make = raw_input("Player 2, please enter your car: ")

while p2_make != "BMW" and p2_make != "Porsche" and p2_make != "Ferrari":
    p2_make = raw_input("Invalid entry choose either BMW, Porsche, or Ferrari: ")

p2_driver = raw_input("Player 2, please eter your driver: ")

while p2_driver != "Mario Andretti" and p2_driver != "Tony Stewart":
    p2_driver = raw_input("Invalid entry choose either Mario Andretti or Tony Stewart: ")
    
player1 = Car(p1_make,p1_driver)
player2 = Car(p2_make,p2_driver)

lap = 1

#run the drive() function until a car has more than 500 miles

while player1.miles < 500 and player2.miles < 500:
    player1.drive()
    player2.drive()
    print "Lap",lap
    print "Player 1 has driven",player1.miles,"miles."
    print "Player 2 has driven",player2.miles,"miles."
    lap += 1

#print a message informing the players whose car won.

if player1.miles >= 500 and player2.miles >= 500:
    if player1.miles > player2.miles:
        print "Congratulations! Player 1 with",player1.driver,"driving a",player1.make+", you are the winner!"
    else:
        print "Congratulations! Player 2 with",player2.driver,"driving a",player2.make+", you are the winner!"

elif player1.miles >= 500:
    print "Congratulations! Player 1 with",player1.driver,"driving a",player1.make+", you are the winner!"

else:
    print "Congratulations! Player 2 with",player2.driver,"driving a",player2.make+", you are the winner!"
    
raw_input("\nPress enter to exit.")




        
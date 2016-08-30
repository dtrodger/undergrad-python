

#create a class Television that takes a channel num volume num and status input

class Television(object):
    
    def __init__(self, channel, volume, is_on):
        self.channel = channel
        self.volume = volume
        self.is_on = is_on.lower()

    def __str__(self):
        if self.is_on == "on":
            reply = "Television on\n"
            reply += "Your watching channel "+str(self.channel)+"\n"
            reply += "The volume is at level "+str(self.volume)

            return reply
        else:
            reply = "The television is off"

            return reply

#defines a function that toggles the is on to off/on

    def toggle_power(self):
        if self.is_on == "on":
            self.is_on = "off"
        else:
            self.is_on = "on"

# returns the current channel

    def get_channel(self):
        print self.channel

# Can you tell me why this if statement always returns the else when i add the and conditions?

##    def set_channel(self, number):
##        if self.is_on == "on" and number >= 0 and number < = 499:
##            self.channel = number
##        else:
##            print "Unable to change the channel."

#changes the channel

    def set_channel(self, number):
        if self.is_on == "on" :
            self.channel = number
        else:
            print "Unable to change the channel."

#raises the volume

    def raise_volume(self):
        if self.volume == 10:
            print "Volume level at maximum"
        else:
            self.volume += 1

#lowers the volume

    def lower_volume(self):
        if self.volume == 0:
            print "Volume level at its minimum"
        else:
            self.volume -= 1

#creates a Television class and lets the user toggle the power
#change the channel and change the volume

def main():
    tv = Television(1, 5, "on")
    choice = ""
    while choice != "0":
        print \
              """
                0 - Exit
                1 - Toggle Power
                2 - Change Channel
                3 - Raise Volume
                4 - Lower Volume

                """
        choice = raw_input("Choice: ")


        if choice == "0":
            print "Goodbye"

        elif choice == "1":
            tv.toggle_power()
            print tv

        elif choice == "2":
            channel = raw_input("Please enter a channel to change to: ")
            tv.set_channel(channel)
            print tv

        elif choice == "3":
            tv.raise_volume()
            print tv

        elif choice == "4":
            tv.lower_volume()
            print tv

        else:
            print "Sorry invalid choice"

main()
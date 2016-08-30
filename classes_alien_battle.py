
#Alien Blaster

#create a player class
class Player(object):

#allow the class to take in a number of bullets

    def __init__(self, ammo):
        self.ammo = ammo

#attack the alien
        
    def blast(self, enemy):

#if the player is out of ammo tell him to run
        
        if self.ammo == 0:
            print "The player is out of ammo. Run!\n"

#if the player has ammo subtract 1 from his ammo count tell him he
#blasted the alien and call a method that subtracts one from the aliens life
            
        else:
            self.ammo -= 1
            print "The player blasts an enemy.\n"
            enemy.die()

#create a alien class

class Alien(object):

#allow the class to take in a number that repressents the aliens life

    def __init__(self, life):
        self.life = life

#create a method that simulates the alien being shot

    def die(self):

#if the alien is already dead respond saying so
        
        if self.life < 1:
            print "Oww im already dead...\n"

#if this shot killed the alien respond saying so and subtract one from his life
            
        elif self.life == 1:
            print "The alien gasps and says, 'Oh,this is it. This is the big one. \n"\
                  "Yes, it's getting dark now. Tell my 1.6 million larvae that I"\
                  "loved them... Good-bye, cruel universe.'\n"
            self.life -= 1

#if the alien is still alive after being shot respond saying so and subtract one from his life
        else:
            print "The Invader responds 'Im not dead yet!'\n"
            self.life -= 1
#main

print "\t\tDeath of an Alien\n"

hero = Player(2)
invader = Alien(1)
hero.blast(invader)

print "\n\nNew game\n\n"

hero2 = Player(1)
invader2 = Alien(2)
hero2.blast(invader2)
hero2.blast(invader2)

print "\n\nNew game\n\n"

hero3 = Player(2)
invader3 = Alien(0)
hero3.blast(invader3)
hero3.blast(invader3)

print "\n\nNew game\n\n"

hero4 = Player(1)
invader4 = Alien(100)
hero4.blast(invader4)
hero4.blast(invader4)

raw_input("\n\nPress the enter key to exit.")
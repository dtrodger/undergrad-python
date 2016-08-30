# David Rodgers
# Extra Credit

#weapon class that have attribute with damage value
class Weapon(object):

    def __init__(self, damage = 0):
        self.damage = damage

#child of weapon that allows user to swing the weapon and display damage
class Sword(Weapon):

    def swing(self):
        print "You swing and inflict "+str(self.damage)+" damage points.\n"

#child of weapon with an attribute to tell in the weapon is loaded
class Crossbow(Weapon):

    def __init__(self, damage):
        super(Crossbow, self).__init__(damage)
        self.is_loaded = True

#fires the weapon
    def fire(self):
        if self.is_loaded:
            self.is_loaded = False
            print "You fire and inflict "+str(self.damage)+" damage points.\n"
        else:
            print "You must reload before you fire again.\n"

#relaods the weapon
    def reload_bow(self):
        if self.is_loaded:
            print "Already loaded.\n"
        else:
            print "Loaded.\n"
            self.is_loaded = True
                
sword = Sword(5)
sword.swing()
sword.swing()
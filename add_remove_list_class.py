
#Player

# creates a Player class that takes a name max item number and list of
# items as inputs

class Player(object):
    """A player who can carry limited objects"""
    
    def __init__(self, name, max_items, items):
        self.name = name
        self.max_items = max_items
        self.items = items

#prints the inventory
        
    def inventory(self):
        if self.items == []:
            print "You have no items in your inventory\n"
        else:
            print "\nInventory includes:"
            for item in self.items:
                print item+" "

#adds a new item to the inventory
                
    def take(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
            print "\n"+item+" added to inventory."
        else:
            print "\nYou cannot carry any more items."

#removes an item from the inventory
            
    def drop(self, item):
        if item in self.items:
            self.items.remove(item)
            print "\n"+item+" removed from inventory."
        else:
            print "\nYou are not carrying that item."


#main
player1 = Player("Joe",3,[] )
player1.take("Ball")
player1.inventory()
player1.take("Bag")
player1.inventory()
player1.take("Shoe")
player1.inventory()
player1.take("Bat")
player1.inventory()
player1.drop("Sock")
player1.drop("Bag")
player1.inventory()

        


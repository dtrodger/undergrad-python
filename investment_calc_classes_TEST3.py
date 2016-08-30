#David Rodgers
#Practical 3


#create a class to hold info about investments

class Investment(object):

    investment_list = []

#static method that prints all the investments

    @staticmethod
    def print_all():
        print "Current Investments are:"
        for investment in Investment.investment_list:
            print "Investment: "+investment.name
            print "   Initial Balance: "+str(investment.initial_balance)
            print "   Current Balance: "+str(investment.current_balance)
            print

#static method that prints the investments that lost money

    @staticmethod
    def print_losers():
        losers = []
        for investment in Investment.investment_list:
            if investment.initial_balance > investment.current_balance:
                losers.append([investment])
        if losers != []:
            print "The Losing Investments are:"
            for investments in losers:
                for losing_inv in investments:
                    print "Investment: "+losing_inv.name
                    print "   Initial Balance: "+str(losing_inv.initial_balance)
                    print "   Current Balance: "+str(losing_inv.current_balance)
                    print
        else:
            print "All your investments are up."

#static method that prints the investment with the lowest current balance

    @staticmethod
    def smallest():
        smallest = Investment.investment_list[0]
        for investment in Investment.investment_list:
            if investment.current_balance < smallest.current_balance:
                smallest = investment
        print "The Smallest Investment Is:"
        print "Investment: "+smallest.name
        print "   Initial Balance: "+str(smallest.initial_balance)
        print "   Current Balance: "+str(smallest.current_balance)
        print

#new investments need name and balance input. current balance is = to initail

    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = float(initial_balance)
        self.current_balance = float(initial_balance)
        Investment.investment_list.append(self)

#return the info about the investment

    def __str__(self):
        reply = "Investment:"+self.name
        reply += "\n  Initial balance: "+str(self.initial_balance)
        reply += "\n  Current balance: "+str(self.current_balance)+"\n"
        return reply

#compare the current balance of two investments

    def __cmp__(self, other):
        if self.current_balance > other.current_balance:
            return True
        else:
            return False

#swap the current balances of two investments

    def swap(self, other):
        print "Swapping "+self.name+" for "+other.name+".\n"
        self.current_balance,other.current_balance = other.current_balance, self.current_balance


#SavingsAccount class that is a child of Investments

class SavingsAccount(Investment):

#attributes of class are name initial balance current balance and IR

    def __init__(self, name, initial_balance, interest_rate):
        super(SavingsAccount, self).__init__(name, initial_balance)
        self.current_balance = self.initial_balance
        self.interest_rate = interest_rate

#return the information about the savings account

    def __str__(self):
        reply = "SavingsAccount Investment: "+self.name+"\n"
        reply += "  Initial Balance: $"+str(self.initial_balance)+"\n"
        reply += "  Current Balance: $"+str(self.current_balance)+"\n"
        reply += "  Interest Rate:  %"+str(self.interest_rate)+"\n"
        return reply

#update the current balance account annually

    def annual_update(self):
        if self.current_balance < 1000:
            self.current_balance -= 10
        else:
            self.current_balance = self.current_balance + (self.current_balance * (self.interest_rate * .01))
        



    
#Test Code for Part 1
gold = Investment("Gold",800.37)
pork = Investment("Pork Bellies",225.59)
apple = Investment("Apple Stock",735.24)

print "Welcome to the I210 Investment Tracker."
print "(This version was coded by David Rodgers",
print ", with username 'dtrodger')\n"
print "-"*60

pork.current_balance += 100.34

print pork
print apple > gold, "\n"
gold.swap(pork)
print gold

#Test Code for Part 2

pork.current_balance += 100.34
apple.current_balance -= 200.99
gold.current_balance += 50.04

Investment.print_all()
Investment.smallest()
gold.swap(pork)
Investment.print_losers()

# Test code for part 3

account1 = SavingsAccount("IUCU",900.05,4)

print account1

print "This account loses money the first year."
account1.annual_update()
print account1

print "$200.56 is deposited:"
account1.current_balance += 200.56
print account1

print "After 10 years."
for i in range(10):
    account1.annual_update()

print account1

#Code written as an attempt at the extra credit. I also changed all the
#current_balance calls to __current_balance but I couldnt figure it out.

##    @property
##    def current_balance(self):
##        return self.__current_balance
##
##    @current_balance.setter
##    def current_balance(self, new):
##        if (self.__current_balance - new) <= 0:
##            print "No single transaction may empty an investment."
##        else:
##            print "Transaction allowed"
##            self.current_balance -= new 
#David Rodgers
#I210 Practical 4

#import GUI stuff
from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

#create the widgets on the GUI
    def create_widgets(self):
        
        #1st row
        self.lbl1 = Label(self, text="Estimate Your Loan:")
        self.lbl1.grid(row = 0, column = 1)

        #2nd row
        self.lbl2 = Label(self, text="Customer Name:")
        self.lbl2.grid(row = 1, column = 0, sticky = E)
        self.name = Entry(self, width = 50)
        self.name.grid(row = 1, column = 1, sticky = W)
        self.bttn1 = Button(self, text = "Calculate!", command = self.text)
        self.bttn1.grid(row = 1, column = 2)

        #3rd row
        self.lbl3 = Label(self, text="Customize the Car:")
        self.lbl3.grid(row = 2, column = 1)

        #4th row
        self.lbl4 = Label(self, text="Choose Brand:")
        self.lbl4.grid(row = 3, column = 0)
        self.lbl5 = Label(self, text="Choose Type:")
        self.lbl5.grid(row = 3, column = 1)
        self.lbl6 = Label(self, text="Choose Options:")
        self.lbl6.grid(row = 3, column = 2)
        
        #Brands radio
        self.brand = StringVar()
        self.brand.set(None)
        Radiobutton(self, text = "Ford ($18,000)", variable = self.brand, value = "Ford").grid(row = 4, column = 0, sticky = W)
        Radiobutton(self, text = "Nissan ($26,000)", variable = self.brand, value = "Nissan").grid(row = 5, column = 0, sticky = W)
        Radiobutton(self, text = "BMW ($40,000)", variable = self.brand, value = "BMW").grid(row = 6, column = 0, sticky = W)
        Radiobutton(self, text = "Tesla ($50,000)", variable = self.brand, value = "Tesla").grid(row = 7, column = 0, sticky = W)

        #Type radio
        self.type = StringVar()
        self.type.set(None)
        Radiobutton(self, text = "Budget (-15%)", variable = self.type, value = "budget").grid(row = 4, column = 1)
        Radiobutton(self, text = "Mid-Range (+5%)", variable = self.type, value = "mid-range").grid(row = 5, column = 1)
        Radiobutton(self, text = "Luxury (+20%)", variable = self.type, value = "luxury").grid(row = 6, column = 1)

        #Options check
        self.option1 = BooleanVar()
        self.option2 = BooleanVar()
        self.option3 = BooleanVar()
        Checkbutton(self, text = "Alloy Wheels (+$1000)",variable = self.option1).grid(row = 4, column = 2)
        Checkbutton(self, text = "Leather Interior (+$2000)",variable = self.option2).grid(row = 5, column = 2)
        Checkbutton(self, text = "Satellite Radio (+$500)",variable = self.option3).grid(row = 6, column = 2)

        #row 8-10
        self.lbl7 = Label(self, text = "Money Down:").grid(row = 8, column = 1)
        self.money_down = Entry(self, width = 10)
        self.money_down.grid(row = 9, column = 1)
        self.text = Text(self, width = 70, height = 10, wrap = WORD)
        self.text.grid(row = 10, column = 0, columnspan = 3)

#update the text box
    def text(self):

        #update with user name brand of car and type
        reply = "Thanks for shopping with us, " + self.name.get() +".\n"
        reply += "Your car is a "+self.type.get()+" "+self.brand.get()
        if self.option1.get() and self.option2.get() and self.option3.get():
            reply += " with alloy wheels, leather interior, and satillite radio."
        elif self.option1.get() and self.option2.get():
            reply += " with alloy wheels, and leather interior."
        elif self.option1.get() and self.option3.get():
            reply += " with alloy wheels, and satillite radio."
        elif self.option2.get() and self.option3.get():
            reply += " with leather interior, and satillite radio."
        elif self.option1.get():
            reply += " with alloy wheels."
        elif self.option2.get():
            reply += " with leather interior."
        elif self.option3.get():
            reply += " with satillite radio."
        else:
            reply += "."

        #calculate the cost
        val = float(0)

        if self.brand.get() == "Ford":
            val += 18000
        elif self.brand.get() == "Nissan":
            val += 26000
        elif self.brand.get() == "BMW":
            val += 40000
        elif self.brand.get() == "Telse":
            val += 50000
            
        if self.type.get() == "budget":
            val = val*.85
        if self.type.get() == "mid-range":
            val = val*1.05
        if self.type.get() == "luxury":
            val = val*1.2

        if self.option1.get():
            val += 1000
        if self.option2.get():
            val += 2000
        if self.option3.get():
            val += 500

        #return the cost
        reply +="\nThe total price is $"+str(val)+"."
        reply +="\nYou will need to borrow $"+str(val - int(self.money_down.get()))

        #calculate and return the monthly payments
        month_pay = ((val - int(self.money_down.get()))*1.05)/48
        reply +="\nAt 5% interest, over 4 years of payments, your monthly payment will be $"+str(round(month_pay,2))
            
        self.text.delete(0.0,END)
        self.text.insert(0.0,reply)


# main
root = Tk()
root.title("Car Loan Estimator")
root.geometry("577x450")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
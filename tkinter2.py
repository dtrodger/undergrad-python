#import GUI element
from Tkinter import *

class Application(Frame):

#define elements in the GUI
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

#create buttons with text displaying their grid location
    def create_widgets(self):
        self.bttn1 = Button(self, text="Row = 0\nColumn = 0")
        self.bttn1.grid(row = 0, column = 0)
        self.bttn1 = Button(self, text="Row = 1\nColumn = 0")
        self.bttn1.grid(row = 1, column = 0)
        self.bttn1 = Button(self, text="Row = 2\nColumn = 0")
        self.bttn1.grid(row = 2, column = 0)
        self.bttn1 = Button(self, text="Row = 0\nColumn = 1")
        self.bttn1.grid(row = 0, column = 1)
        self.bttn1 = Button(self, text="Row = 1\nColumn = 1")
        self.bttn1.grid(row = 1, column = 1)
        self.bttn1 = Button(self, text="Row = 2\nColumn = 1")
        self.bttn1.grid(row = 2, column = 1)
        self.bttn1 = Button(self, text="Row = 0\nColumn = 2")
        self.bttn1.grid(row = 0, column = 2)
        self.bttn1 = Button(self, text="Row = 1\nColumn = 2")
        self.bttn1.grid(row = 1, column = 2)
        self.bttn1 = Button(self, text="Row = 2\nColumn = 2")
        self.bttn1.grid(row = 2, column = 2)


# main
root = Tk()
root.title("Grid Layout")
root.geometry("220x120")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
#David Rodgers

#import the tools program
import tools

#from the people.txt file, read the lines then strip and split each line

names = [name.strip().split() for name in open("people.txt","r").readlines()]

#input the names from the list comp into the table print funciton from tools
tools.table_print(["Name","Age"], names)
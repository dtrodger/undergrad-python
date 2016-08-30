# David Rodgers
# Individual HW 8



# define a class People that takes names and phone numbers as inputs

class People(object):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# define a class Employee thats a child class of People with a salary input

class Employee(People):

# keep track of the sum of all employees salaries within a global variable

    total_salary = 0

    def __init__(self,name, phone, salary):
        super(Employee,self).__init__(name, phone)
        self.salary = salary
        Employee.total_salary += salary

    def __str__(self):
        reply = "Person "+self.name+" has phone "+self.phone
        reply += "\n  and is an Employee with salary "+str(self.salary)
        return reply
        
# define a class Student thats a child class of People with a gpa input

class Student(People):

    all_gpa = []

    def __init__(self, name, phone, gpa):
        super(Student,self).__init__(name, phone)
        self.gpa = gpa
        Student.all_gpa.append(gpa)

    def __str__(self):
        reply = "Person "+self.name+" has phone "+self.phone
        reply += "\n  and is a Student with gpa "+str(self.gpa)
        return reply

# define a function the returns the average gpa of all students

    @staticmethod
    def mean_gpa():
        sum_gpa = 0
        for gpa in Student.all_gpa:
            sum_gpa += gpa
        mean_gpa = sum_gpa / len(Student.all_gpa)
        return mean_gpa

# define a class Staff thats a child class of Employee with a title input

class Staff(Employee):

    def __init__(self, name, phone, salary, title):
        super(Staff,self).__init__(name, phone, salary)
        self.title = title

    def __str__(self):
        reply = "Person "+self.name+" has phone "+self.phone
        reply += "\n  and is an Employee with salary "+str(self.salary)
        reply += "\n  and is a Staff with Title "+self.title
        return reply
        
# define a class Professor thats a child class of Employee with a course input

class Professor(Employee):

    def __init__(self, name, phone, salary, course):
        super(Professor,self).__init__(name, phone, salary)
        self.course = course

    def __str__(self):
        reply = "Person "+self.name+" has phone "+self.phone
        reply += "\n  and is an Employee with salary "+str(self.salary)
        reply += "\n  and is a Professor assigned to class "+self.course
        return reply

# Create a list of people

People = [ Student("Sandy", "326-8324", 3.65), Student("Jordan", "632-7434", 3.1), \
           Professor("Leslie", "985-2363", 50000.00, "Info 501"),  \
           Staff("Alex", "743-4638", 25000.00, "Editor") ]

# display the information about our people

print "These are the people in the university:"
for person in People:
   print person

# display the total salaries of all our employees and average GPA of students

print
print "Our total university payrol budget is: " + str(Employee.total_salary)
print "Our average student GPA is: " + str(Student.mean_gpa())

    
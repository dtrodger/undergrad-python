#David Rodgers
#INFO I 211 Practical 2


import urllib, re, webbrowser

#open and read the contents of the web page
web_page = urllib.urlopen("http://www.soic.indiana.edu/undergraduate/courses/index.html")
contents = web_page.read()
web_page.close

print "Paresing: http://www.soic.indiana.edu/undergraduate/courses/index.html\n"

#find all the sections of links that contain class names
classes_extra = re.findall('department=[\w]+">[\w ,/-]+',contents)

classes = []

#append the class name alone to a list and print it
for tech_class in classes_extra:
    class_name_extra = re.findall('>[\w ,/-]+',tech_class)
    class_name = class_name_extra[0].replace(">","")
    print class_name
    classes.append(class_name)

print "\nParesing: http://www.soic.indiana.edu/undergraduate/courses/index.html\n"

#ask the user for a word to search for in the class names
user_parse = raw_input("Please enter a word to search for: ")
print

#find all classes that contain that word
matching_parsed = [tech_class_parsed for tech_class_parsed in classes\
                        if user_parse in tech_class_parsed]

#print all classes that contain that word
for parsed_class in matching_parsed:
    print parsed_class

#ask the user to pick a class whose page they want to open
user_course_num = raw_input("\nEnter the name of a course (Ex: I210) to view it, or Press ENTER: ")

#if the user presses enter tell them no input was given
if user_course_num == "":
    print "No input was given"

else:
    #if the user input a class find that class in the matched classes
    for course in matching_parsed:
        if user_course_num in course:
            user_parsed_full_course = course

            #get the class info into the right format for the url
            user_prefix_lower = user_course_num[0].lower()
            user_end = user_course_num[1:4]

            #add the class info into the soic url
            soic_class_url = "https://www.soic.indiana.edu/undergraduate/courses/"\
                             "index.html?number="+user_prefix_lower+user_end\
                             +"&department="+user_parsed_full_course[0:4]

            #open the page
            webbrowser.open_new_tab(soic_class_url)

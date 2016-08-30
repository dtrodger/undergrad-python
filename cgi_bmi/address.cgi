#! /usr/bin/env python

print 'Content-type: text/html\n'

import cgi

html = """
<html>
<body>
    <p>Name: {user_name}</p>
    <p>Address:</p>
    <p>{user_add1}</p>
    <p>{user_add2}, {user_state}, {user_zip}</p>
</body>
</html>
"""

error_html = """
<html>
<body>
<p>Please go back and fill in all the fields</p>
</body>
</html>
"""

form = cgi.FieldStorage()

name = form.getfirst('fname')
add1 = form.getfirst('add1')
add2 = form.getfirst('add2')
city = form.getfirst('city')
state = form.getfirst('state')
zipcode = form.getfirst('zip')


if name is not None and add1 is not None and city is not None\
   and state is not None and zipcode is not None:
    txt = open('address.txt','a')
    string = '\n'+str(name)+', '+str(add1)+', '
    if add2 != None:
        string += str(add2)+', '
    string += str(city)+', '+str(zipcode)
    txt.write(string)
    txt.close()
    if add2 != None:
        print html.format(user_name = name, user_add1 = add1,\
                      user_add2 = add2, user_state = state,\
                      user_zip = zipcode)
    else:
        print html.format(user_name = name, user_add1 = add1,\
                      user_add2 = '', user_state = state,\
                      user_zip = zipcode)
else:
    print error_html
        
        

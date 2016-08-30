#! /usr/bin/env python

print 'Content-type: text/html\n'

import MySQLdb, cgi

form = cgi.FieldStorage()

plantID = form.getfirst("PlantID","")
commonname = form.getfirst("common")
basename = form.getfirst("base")
price = form.getfirst("price")

html = """
<html>
<body>

<h1> Faculty Table </h1>

<form action='PlantBuyAction.cgi'method="get">
	<input type="hidden" value="{PlantID}" name="PlantID">
	Buyer: <input type="text" name="name" /><br />
	Common Name: {common}<br />
	Base Name: {base}<br />
	Price: ${price}<br />
	Quantity: <input type="text" name="quantity"/><br/>
	<input type="reset" value="Reset All Fields">&nbsp;&nbsp;&nbsp;
	<input type="submit" value="Make Purchase"><br />
</form>
</body>
</html>
"""
print html.format(PlantID = plantID, common = commonname, base = basename, price = price)



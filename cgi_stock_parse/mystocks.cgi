#! /usr/bin/env python

print 'Content-type: text/html\n'

import cgi, urllib, csv, re

html = """
<html>
<body>
<table border="1" width="40%">
    <tbody>
        <tr>
            <th>Name</th><th>Price</th><th>Change</th><th>Volume</th>
            <th>Change</th>
        </tr>
        {stocks_table}
    </tbody>
</table>
</body>
</html>"""

form = cgi.FieldStorage()

stocks = form.getfirst("stocks","")
stocks = re.findall('[\w]+', stocks)

baseurl = "http://quote.yahoo.com/d/quotes.csv?s={0}&f=sl1d1t1c1ohgvj1pp2owern&e=.csv"

html_new = ""

for stock in stocks:
	url = baseurl.format(stock)
	web_page = urllib.urlopen(url)
	read = csv.reader(web_page)
	row = read.next()
	web_page.close()

	html_new += "<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[4])+\
	"</td><td>"+str(row[8])+"</td><td>"+str(row[11])+"</td></tr>"

print html.format(stocks_table = html_new)


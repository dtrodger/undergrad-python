#! /usr/bin/env python

print 'Content-type: text/html\n'

import MySQLdb, cgi

form = cgi.FieldStorage()

buyername = form.getfirst("name")
plantID = form.getfirst("PlantID")
quantity = form.getfirst("quantity")

def results_table(records):
    #display data from DB
    print "<html><body><table border='1' width='100%'>"
    print "<tr><th>TransactionID</th><th>Buyer</th><th>PlantID</th><th>Quantity</th></tr>"
    for row in records:
            print "<tr>"
            for i in range(len(row)):
                print "<td  align='center'>", row[i],"</td>"
            print "</tr>"
    print "</table></body></html>"

#establish DB connection
string = "i211f15_dtrodger" 	#change this to yours
password = "my+sql=i211f15_dtrodger"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

try:				#Always surround .execute with a try!
        SQL = "Insert into Transactions values ('',"+str(buyername)+","+str(plantID)+","+str(quantity)+");"
        cursor.execute(SQL)
        db_con.commit()            

except Exception, e:		#Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print "\nError:", e

print "<h1>Purchases</h1>"
try:
        SQL = "SELECT * FROM Transactions; "
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception, e:        #Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print SQL
        print "\nError:", e
else:               #This runs if there was no error
        results_table(results)
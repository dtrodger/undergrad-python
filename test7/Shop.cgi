#! /usr/bin/env python

print 'Content-type: text/html\n'

import MySQLdb, cgi

print "<h1>Welcome to the Plant Shop</"

def results_table(records):
    #display data from DB
    print "<html><body><table border='1' width='100%'>"
    print "<tr><th>PlantID</th><th>CommonName</th><th>BotanicalName</th><th>Price</th><th></th></tr>"
    for row in records:
            print "<tr>"
            for i in range(len(row)):
                print "<td  align='center'>", row[i],"</td>"
            print "<td><a href='PlantBuy.cgi?PlantID="+str(row[0])+"&common="+str(row[1])+"&base="+str(row[2])+"&price="+str(row[3])+"'>Buy</a></td>"
            print "</tr>"
    print "</table></body></html>"

string = "i211f15_dtrodger" 	#change this to yours
password = "my+sql=i211f15_dtrodger"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

try:
        SQL = "SELECT * FROM Plants; "
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception, e:		#Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print SQL
        print "\nError:", e
else:				#This runs if there was no error
        results_table(results)
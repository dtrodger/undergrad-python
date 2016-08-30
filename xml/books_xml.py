#David Rodgers
#INFO I 211

import xml.etree.ElementTree as ET

#parse the xml then find the distinct cds
root = ET.parse(source="cd_catalog.xml")

cds = root.findall("CD")

#find the min and max price by comparing the price of each
#cd to the min max values. if current price lower or higher
#replace min or mx with current price
cd_min = 0
cd_max = 0

for cd in cds:
    this_cd_cost = float(cd.find('PRICE').text)

    if cd_min == 0:
        cd_min = this_cd_cost

    if this_cd_cost < cd_min:
        cd_min = this_cd_cost
        
    if this_cd_cost > cd_max:
        cd_max = this_cd_cost

#find the number of cds in the xml
print "There are",len([cd for cd in cds]),"CDs on file."

#find the cost of purchasing all cds in the xml
print "Total price of purchasing each CD: $",\
      sum([float(cd.find('PRICE').text) for cd in root.findall("CD")])

print "The cheapest CD costs: $",cd_min

print "The most expensive CD costs: $",cd_max

#find the average price of a cd
print "The average price of a CD is: $",round(sum([float(cd.find('PRICE').text)\
                                                   for cd in root.findall("CD")])\
                                              /len([cd for cd in cds]), 2)

#find the number of cds released in 1990
print len([cd for cd in cds if cd.find('YEAR').text == "1990"]),\
      " CDs in the file were released in 1990"

#find the artists who released their cd in the USA
print "\nAmerican artists on file include:"
for artist in [cd.find("ARTIST").text for cd in cds if\
               cd.find('COUNTRY').text == "USA"]:
    print artist
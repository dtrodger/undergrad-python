#David Rodgers
#INFO I 211 Practical 3


import urllib, xml.etree.ElementTree as ET, re

#read the contents of a web page then convert the contents into XML
web_page = urllib.urlopen("https://cgi.soic.indiana.edu/~dpierz/shop.html")
content = web_page.read()
web_page.close()

elements = ET.XML(content).getiterator()

menu_items = []

#find all the tr tags in the XML and save their childerns text as elements
#in a list
for elem in elements:
    if elem.tag == "tr":
        attribs = list(elem)
        menu_items.append((attribs[0].text,attribs[1].text,\
                       attribs[2].text))

#remove the info from the head of the table
menu_items = menu_items[1:]

print menu_items
print

#define a function that takes in a list and adds the elements in the list
#into an xml document
def add_xml_class(item_info):
    tree = ET.parse(source="shop.xml")
    root = tree.getroot()
    new_entry = ET.SubElement(root, 'entry')
    new_name = ET.SubElement(new_entry,'name')
    new_name.text = item_info[0]
    new_options = ET.SubElement(new_entry, 'options')
    new_options.text = item_info[1]
    new_price = ET.SubElement(new_entry,'price')
    new_price.attrib['currency'] = 'dollars'
    new_price.text = item_info[2]

    tree.write('shop.xml')
    print "New entry added."

#call the function over the list of menu items
for item in menu_items:
    add_xml_class(item)

#EXTRA CREDIT

#parse the xml menu items file
root = ET.parse(source="shop.xml")

#find all the entries
ec_item = root.findall('entry')

#sum the price of each for total
total = sum([float(item.find('price').text[1:]) for item\
                          in ec_item])

#print total
print "Total price: $",total

#find average cost by dividing total cost by the len of the item list
print "Average price: $",round((total/len(ec_item)),2)
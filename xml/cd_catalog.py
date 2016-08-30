#David Rodgers
#INFO I211

import xml.etree.ElementTree as ET

#parse the xm
tree = ET.parse(source="books.xml")

def book_info(id_num):
    #find the books in the xml tree
    books = tree.findall('book')

    #find the book with the matching id as the input
    #return info about the book
    for book in books:
        if book.attrib['id'] == id_num:
            print "Info for book with ID:",id_num,"\n",\
                  "Title:",book.find('title').text,"\n",\
                  "Author:",book.find('author').text,"\n",\
                  "Price: $",float(book.find('price').text),"\n"

#call the function on every book id in the xml file
part_a_call = [book_info(book_id) for book_id in\
               [book.attrib['id'] for book in tree.findall('book')]]

#find the cost of buying all the books
print "The cost of purchasing all books in the Computer genre is $",\
      sum([float(book.find('price').text) for book in tree.findall('book')\
                      if book.find('genre').text == "Computer"])

#find the unique genres in the xml file
genres = []
[genres.append(book.find('genre').text) for book in tree.findall('book') if book.find('genre').text\
          not in genres]
print "The unique genres in the file are:"
for genre in genres:
    print genre
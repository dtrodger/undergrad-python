#David Rodgers
#INFO I 211 - Individual HW 5

import urllib, csv, datetime, re



def getStockData(company = "GOOG"):

#open a the yahoo finance url with the comapny ticker in it. read it into
#csv then close it
    web_page = urllib.urlopen("http://quote.yahoo.com/d/quotes.csv?s="+\
                              company+"&f=sl1d1t1c1ohgvj1pp2owern&e=.csv")
    read = csv.reader(web_page)
    row = read.next()
    web_page.close()

#format the change data
    pointless_format_req_in_hw = str(row[4])
    pointless_format_req_in_hw = pointless_format_req_in_hw.replace(pointless_format_req_in_hw[0],\
                                       pointless_format_req_in_hw[0]+"$")

#split the date on / and set it into the right format
    date = row[2]
    date = date.split("/")
    date_datetime = datetime.date(int(date[2]),int(date[0]),int(date[1]))
    format_date = date_datetime.strftime("%b, %d %Y")

#return the string with the stock data
    print "\nThe last trade for "+str(row[0])+" was "+str(row[1])+" and the change was "+pointless_format_req_in_hw+" on "+format_date+". The open was "+str(row[5])+" and the previous close was "+str(row[10])+"."

def tickerFinder(page = "http://www.fool.com/the-25-best-companies-in-america/index.aspx"):

#open the url containing tickers. read the contents. close it.
    web_page = urllib.urlopen(page)
    contents = web_page.read()
    web_page.close()

#parse the content for tickers
    tickers = re.findall("Ticker/[\w-]+",contents)

#format the ticker then input it into the StockData function
    for ticker_unformat in tickers:
        ticker = ticker_unformat[7:]

        getStockData(ticker)

#main
        
companies = ["AAPL","GOOG","GM","POT","BUD","WBA","W","WYNN","WFM","GWW"]

for company in companies:
    getStockData(company)

print "\n"+"-"*30+"EXTRA CREDIT BEGINS"+"-"*30

tickerFinder()
    
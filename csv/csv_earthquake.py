import csv, datetime

def earthquakeInfo(src, mag):

        quake_dict = csv.DictReader(open('2.5_week.csv', 'r'))

        today_date = datetime.date.today()

        quakes_week = 0
        quakes_yesterday = 0
        quakes_source = 0
        
        for entry in quake_dict:
            if round(float(entry['mag']),0) == float(mag):
                if int(entry['time'][8:10]) > int(today_date.strftime("%d"))-8:
                    quakes_week += 1
                if int(entry['time'][8:10]) > int(today_date.strftime("%d"))-1:
                    quakes_yesterday += 1
                if entry['net'] == src:
                    quakes_source += 1

        if quakes_week == 0:
            print "No earthquakes with magnitude",mag,"found."
        else:
            print "Todays date: "+today_date.strftime("%Y-%m-%d")
            print "Total number of magnitude",mag,"Earthquakes past 7 days: "\
          +str(quakes_week)
            print "Earthquakes with magnitude",mag,"yesterday: "+\
                  today_date.strftime("%Y-%m-")+\
                  str((int(today_date.strftime("%d")) - 1))+": "+\
                  str(quakes_yesterday)
            print "Earthquakes with magnitude",mag,"source",src,":",\
                  quakes_source

        
                

earthquakeInfo('ak','3')
earthquakeInfo('us','7')
earthquakeInfo('us','20')
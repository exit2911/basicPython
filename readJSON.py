#reading json data feed using provided features

import urllib.request
import json #to read json data feed


    
    
#homepage earthquake.usgs.gov/earthquakes/feed/
#use feed to get info about current earthquake around the world

    

def main():

    urlData =  "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    
    webUrl = urllib.request.urlopen(urlData)

    print("result code: " + str(webUrl.getcode()))

    if(webUrl.getcode()==200): #if read url yiels 200, go ahead and read the data
        data = webUrl.read()
        printResults(data)
    else:
    
        print("error")
    

if __name__ == "__main__": 

    main()
    
def printResults(data):
    theJSON = json.loads(data)
    
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")
    
#json file feature array has multiple properties. outputting the locations
    
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-----------------------")
    
#getting a list of earthquakes with magnitude > = 4.0    
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("-----------------------")
    
    print("events that were felt:")
    
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
               print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],"reported" + str(feltReports) + " times")
        
         


# bringing in html data 

import urllib.request


def main():
    webUrl = urllib.request.urlopen ("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    
    data = webUrl.read() #html code of google home page
    print(data)
    
if __name__ == "__main__": 

    main()
    

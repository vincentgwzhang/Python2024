# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request # instead of urllib2 like in Python 2.7

def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.request.urlopen("https://start.spring.io/actuator/info")
    
    # get the result code and print it
    print ("result code: ", webUrl.getcode())
    
    # read the data from the URL and print it
    data = webUrl.read()
    print (data)

if __name__ == "__main__":
    main()

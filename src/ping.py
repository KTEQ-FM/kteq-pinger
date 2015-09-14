import os
import subprocess as sub
import urllib2
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser


STREAM_URL = "http://kteq-streamer.sdsmt.edu:8000/status.xsl"

def ping(debug=False):
    # Check the Stream
    page = urllib2.urlopen( STREAM_URL )
    soup = BeautifulSoup(page)

    # Check to see if "streamdata" exists
    data = soup.findAll('td', attrs={"class" : "streamdata" })

    # Print out the content I guess
    if debug: 
        print data

    if len(data) > 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    if ping(True):
        print "\n\n\nStream is UP"
    else:
        print "\n\n\nStream is DOWN"

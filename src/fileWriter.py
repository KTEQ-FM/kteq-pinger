from datetime import datetime

PATH = "/home/pi/kteq-pinger/"
FILENAME = "streamStatus.txt"
EMAIL_GOOD = "emailGood.txt"
EMAIL_BAD = "emailBad.txt"

def update(msg):
        #update streamStatus.txt
        f = open( PATH + FILENAME , 'a')
        f.write( msg + timestamp() + "\n" )
        f.close
        #FORGET IT, JUST DIRECTING IO TO FILE
        print msg + timestamp() + "\n"
        return

def getEmail(streamUP = False):
    if streamUP:
        email = EMAIL_GOOD
    else:
        email = EMAIL_BAD
    with open( PATH + email , 'r') as content_file:
        content = content_file.read()
    return content

def timestamp():
    return " @ " + str(datetime.now())


PATH = "../"
FILENAME = "streamStatus.txt"
EMAIL_GOOD = "emailGood.txt"
EMAIL_BAD = "emailBad.txt"

def update(msg):
        #update streamStatus.txt
        f = open( PATH + FILENAME , 'w')
        f.write( msg + "\n" )
        f.close
        return

def getEmail(streamUP = False):
    if streamUP:
        email = EMAIL_GOOD
    else:
        email = EMAIL_BAD
    with open( PATH + email , 'r') as content_file:
        content = content_file.read()
    return content

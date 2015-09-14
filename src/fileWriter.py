
PATH = "../"
FILENAME = "streamStatus.txt"
EMAIL = "email.txt"

def update(msg):
        #update streamStatus.txt
        f = open( PATH + FILENAME , 'w')
        f.write( msg + "\n" )
        f.close
        return

def getEmail():
    with open( PATH + EMAIL , 'r') as content_file:
        content = content_file.read()
    return content

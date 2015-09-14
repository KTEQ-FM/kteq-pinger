import fileWriter

#kteq-pinger's email address
FROM_ADDRESS = "whatever"

#REPLACE "julian.brackins" with whomever is the current Station Engineer.
TO_ADDRESS = ["kteq@mines.sdsmt.edu", "julian.brackins@mines.sdsmt.edu"]

EMAIL_SUBJECT = "KTEQ-PINGER SAYS: KTEQ STREAM IS DOWN :'("

class email:
    def __init__(self, debug=False):
        self.fromAddr = FROM_ADDRESS
        self.toAddr = TO_ADDRESS
        self.msg = fileWriter.getEmail()

    def sendEmail(self):
        #Sending email stuff goes here
        return

    def getMessage(self):
        return self.msg

if __name__ == "__main__":
    e = email(True)
    print "\nHere is the message that will be sent to",
    for email in e.toAddr:
        print email,
    print ":"
    print e.getMessage()    
    

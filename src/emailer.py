import fileWriter


FROM_ADDRESS = "whatever"
TO_ADDRESS = ["kteq@mines.sdsmt.edu", "julian.brackins@mines.sdsmt.edu"]

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
    

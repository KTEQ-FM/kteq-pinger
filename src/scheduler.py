import ping
import fileWriter
import emailer

#other imports
import time

class scheduler:
    def __init__(self, debug=False):
        self.DEBUG = debug        
        self.streamStatus = True
        self.email = emailer.email(self.DEBUG)
        self.fixStream = False

    def run(self):
        if ping.ping(self.DEBUG):
            self.streamStatus = True
            self.check()              
        else:
            self.streamStatus = False
            self.check()
        time.sleep(60)
        return

    def check(self):
        msg = ""
        if self.streamStatus:
            msg = "Stream is Fine"
            #If stream had been down,
            #Send Email notifying it is up
            if self.fixStream:
                self.fixStream = False
                self.post(True)
        else:
            msg = "Stream is Down"
            #Raise flag to fix stream
            self.fixStream = True
            #Send Email notifying stream
            #is down
            self.post(False)
        if self.DEBUG: 
            print msg
        fileWriter.update(msg)
        return

    def post(self, streamUP=False):
        #Here is where the email stuff goes
        self.email.sendEmail(streamUP)
        return

if __name__ == "__main__":
    s = scheduler(True)

    while True:
        try:
            s.run()
        except KeyboardInterrupt:
            print "closing"
            exit(0)


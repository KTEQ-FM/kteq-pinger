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

    def run(self):
        if ping.ping(self.DEBUG):
            self.streamStatus = True              
        else:
            self.streamStatus = False
        self.check()
        time.sleep(60)

    def check(self):
        msg = ""
        if self.streamStatus:
            msg = "Stream is Fine"
            fileWriter.update(msg)
        else:
            msg = "Stream is Down"
            fileWriter.update(msg)
            self.post()
        if self.DEBUG: 
            print msg
        return

    def post(self):
        #Here is where the email error stuff goes
        self.email.sendEmail()
        return

if __name__ == "__main__":
    s = scheduler(True)

    while True:
        try:
            s.run()
        except KeyboardInterrupt:
            print "closing"
            exit(0)


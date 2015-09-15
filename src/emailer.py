import smtplib

import fileWriter
import password

#kteq-pinger's email address
FROM_ADDRESS = "jubear.pi@gmail.com"
FROM_PASS = password.PASSWD

#REPLACE "julian.brackins" with whomever is the current Station Engineer.
TO_ADDRESS = ["kteq@mines.sdsmt.edu", "julian.brackins@mines.sdsmt.edu"]

EMAIL_SUBJECT = ["KTEQ-PINGER SAYS: KTEQ STREAM IS DOWN :'(", "KTEQ-PINGER SAYS: KTEQ STREAM IS UP!! :D"]

class email:
    def __init__(self, debug=False):
        self.fromAddr = FROM_ADDRESS
        self.toAddr = TO_ADDRESS
        self.msg = ""
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

    def sendEmail(self, streamUP = False ):
        #Sending email stuff goes here
        to = ""
        for name in TO_ADDRESS:
          to = to + name + ";"
        header = "To: " + to + "\n" + "From: " + FROM_ADDRESS + "\n" + "Subject: "
        if streamUP:
            header = header + EMAIL_SUBJECT[1]
            self.msg = fileWriter.getEmail(True)
        else:
            header = header + EMAIL_SUBJECT[0]
            self.msg = fileWriter.getEmail(False)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()

        self.smtp.login(FROM_ADDRESS, FROM_PASS)
        self.smtp.sendmail(FROM_ADDRESS, to, header + "\n" + self.msg)
        self.smtp.quit()
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
    e.sendEmail()
    

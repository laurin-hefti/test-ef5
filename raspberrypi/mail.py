import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date, datetime

class Send_email :
    
    def __init__(self):
        self.my_addres = "stockanalyser@web.de"
        self.passwort = "testemailstockapi"

        self.name = "laurin.heft"
        self.email = "laurin.hefti@icloud.com"
        #self.email = "lars.hoesli2@stud.schulegl.ch"
        self.messageTemplate = ""

        self.host = "smtp.web.de"
        self.port = 587

    def server_conection(self):
        s = smtplib.SMTP(self.host, self.port)
        s.starttls()
        s.login(self.my_addres,self.passwort)
        return s

    def create_email(self, msg):
        email = MIMEMultipart()

        email["From"] = self.my_addres
        email["To"] = self.email
        email["Subject"] = "Daily report"

        email.attach(MIMEText(msg,"plain"))

        return email
    
    def send_email(self, msg, form):
        s = self.server_conection()
        msg = self.use_form(form)(msg)
        email = self.create_email(msg)

        s.send_message(email)
        s.quit()

    def form_data(self,data):
        out_str = ""
        out_order = ["Open:     ", 
                     "Close:    ", 
                     "higth:    ",
                     "low:      ",
                     "dif:      ",
                     "p:        "]
        out_str += "End day report\n"
        day = date.today()
        out_str += "at: " + str(day) + "\n"

        for i in range(len(data)):
            out_str += out_order[i] + str(data[i]) + "\n"
        
        out_str += "end"
        
        return out_str
    
    def use_form(self, name):
        forms = [self.form_data]
        forms_name = ["end_day"]

        i = 0

        if name in forms_name:
            i = forms_name.index(name)
        else:
            print("error form not in list")

        return forms[i]

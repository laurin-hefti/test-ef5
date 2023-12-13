import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
import poplib

# ---------------- Email_handler -----------------
# This class handels all Stuff with emails.
# ------------------------------------------------

class Send_email :
    
    def __init__(self):
        self.my_addres = "stockanalyser2@web.de"
        self.passwort = "stockanalyser2"

        self.name = "laurin.hefti"
        self.email = "laurin.hefti@icloud.com"
        self.emails = ["laurin.hefti@icloud.com"]
        self.messageTemplate = ""

        self.host = "smtp.web.de"
        self.port = 587

 # --------- Creating conections to the server -----------
 # smtp for sending emails, and pop for getting emails

    def server_conection_smtp(self):
        s = smtplib.SMTP(self.host, self.port)
        s.starttls()
        s.login(self.my_addres,self.passwort)
        return s
    
    def server_conection_pop(self):
        server = poplib.POP3_SSL("pop3.web.de","995")
        server.user(self.my_addres)
        server.pass_(self.passwort)
        return server
    
# ----------------------------------------------------------

# creates and send emails

    def create_email(self, msg, addres):
        email = MIMEMultipart()

        email["From"] = self.my_addres
        email["To"] = addres
        email["Subject"] = "Daily report"

        email.attach(MIMEText(msg,"plain"))

        return email

    def send_email(self, msg, form):
        s = self.server_conection_smtp()
        for i in range(len(self.emails)):
            msg2 = self.use_form(form)(msg)
            email = self.create_email(msg2, self.emails[i])

            s.send_message(email)
        s.quit()

# ----------------------------------------------------------------

# ---- functions for getting the emails and prcess the data ------
    def get_emails(self):
        server = self.server_conection_pop()
        num_mes = len(server.list()[1])
        mesage_list = server.list()[1]
        cmd = []
        for i in range(num_mes):
            mails = server.retr(i+1)[1]
            for i in mails:
                if "execute" in str(i):
                    cmd.append(i)
        
        #code for deleting the mails but does not work
        for i in mesage_list:
            i = str(i)
            i = i[2:3]
            server.dele(i)
        return cmd
    
    def get_use(self, data):
        only_comand = []
        for i in data:
            i = i.decode()
            if i.index("execute") == 0:
                only_comand.append(i)
        return only_comand
    
    def get_commands(self):
        data = self.get_emails()
        comands = self.get_use(data)
        return comands
    
# ----------------------------------------------------------------------

# ----- function for creating the style of the email -------------------

    def form_data(self,data):
        try:
            out_str = ""
            out_order = ["Open:    ", 
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
        except:
            return "sorry the stock is currently in the Weekend"
    
    def use_form(self, name):
        forms = [self.form_data]
        forms_name = ["end_day"]

        i = 0

        if name in forms_name:
            i = forms_name.index(name)
        else:
            print("error form not in list")

        return forms[i]

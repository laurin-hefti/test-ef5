import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MEINE_ADRESSE = 'stockanalyser@web.de'
PASSWORT = 'testemailstockapi'

def main():
    namen = "laurin.hefti"
    email = "laurin.hefti@icloud.com"
    messageTemplate = "send with python"

    s = smtplib.SMTP(host='smtp.web.de', port=587)
    s.starttls()
    s.login(MEINE_ADRESSE, PASSWORT)

    print("loged in")

    msg = MIMEMultipart() 

    print(messageTemplate)

    msg['From']=MEINE_ADRESSE
    msg['To']=email
    msg['Subject']="Ich lerne Python 3"
    
    msg.attach(MIMEText(messageTemplate, 'plain'))
    
    s.send_message(msg)
        
    s.quit()
    
main()
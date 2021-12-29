import smtplib
from email.message import EmailMessage
from email.header import Header
from email.utils import formataddr
username = input('Enter user username ')
password =input ('Enter your password ')
subject = input('Enter user subject ')
from_name = input('Enter from name ')
# receiver = 'balibhai69@aol.com'
receiver = "balibhai69@aol.com"
import time
emailist = open('email.txt','r')



def send_mails(to):
    
    
    message = EmailMessage()
    message['subject'] = f'{subject}'
    message['from'] = formataddr((str(Header(f'{from_name}', 'utf-8')), f'{username}'))
    message['to'] = to
    html_message = open('templates.html','r').read()
    message.add_alternative(html_message,subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(username, password)
        smtp.send_message(message)
for emails in emailist:
    time.sleep(5)
    email = emails.split(":")
    emailmode = email[0]
    send_mails(emailmode)
    print(emailmode+" message has send to this email")
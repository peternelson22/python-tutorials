import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'peternelson063@gmail.com'
email_password = 'pozjrtlamivygzes'

email_reciever = 'wizendy15@gmail.com'

subject = 'Hello'

body = 'Hello world.....'

e = EmailMessage()
e['From'] = email_sender
e['To'] = email_reciever

e['subject'] = subject
e.set_content(body)

con = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=con) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, e.as_string())
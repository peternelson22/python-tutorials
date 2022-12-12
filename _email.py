from email.message import EmailMessage
import ssl, smtplib
import schedule, time

sender = ''
password = ''

receiver = 'jideabiola@yahoo.com'
subject = 'Hello Jae'
body = 'Hello, how are you!!!!'

_email = EmailMessage()

_email['From'] = sender
_email['To'] = receiver
_email["subject"] = subject
_email.set_content(body)


def send_email_():
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, _email.as_string())


schedule.every(10).seconds.do(send_email_)

while True:
    schedule.run_pending()
    time.sleep(1)

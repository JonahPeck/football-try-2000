from email.message import EmailMessage 
import ssl
import smtplib


email_sender = 'PeckJonahC@gmail.com'
email_password = 'hghm mctd vlpe flql'

email_receiver = input('What email would you like to send to? ')

subject = input('What would you like the subject to be? ')
body = input('What would you like the body to say?')


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


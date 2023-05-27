#!/usr/local/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''Registered
'''

sender_address = 'speedboostvps@gmail.com'
sender_pass = 'aoyptfnpeeltjzym'
receiver_address = 'jamalisaacke@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'vps'

message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'rex'
attach_file = open(attach_file_name, 'rb') 
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) 
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(sender_address, sender_pass) 
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()

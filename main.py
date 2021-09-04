import os
import smtplib
from email.message import EmailMessage

email_account = 'justindzisah@gmail.com'
recipient_account = "officialjdtech@gmail.com"
email_pass = 'ibazoxjtstchildf'

msg = EmailMessage(Hello is this spam)
msg['From']=email_account
msg['To']=recipient_account
msg['subject']='Python Automation'
msg.set_content('''
IS THIS SPAM
''')



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_account, email_pass)
	
	smtp.send_message(msg)

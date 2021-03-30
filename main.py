import os
import smtplib
from email.message import EmailMessage

email_account = 'YOUR EMAIL'
recipient_account = "RECEIVER'S EMAIL"
email_pass = 'APP Password'

msg = EmailMessage()
msg['From']=email_account
msg['To']=recipient_account
msg['subject']='Python Automation'
msg.set_content('''
YOU EMAIL GOES HEAR
''')



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_account, email_pass)
	
	smtp.send_message(msg)

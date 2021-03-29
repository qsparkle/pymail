import os
import smtplib
from email.message import EmailMessage

email_account = 'mobileprogramering@gmail.com'
email_pass = 'niyqnvegeyebfqmn'

msg = EmailMessage()
msg['From']=email_account
msg['To']=email_account
msg['subject']='Python Automation'
msg.set_content('''
Accumsan tortor posuere ac ut consequat semper. At in tellus integer feugiat scelerisque varius morbi. Ipsum consequat nisl vel pretium lectus. Cras sed felis eget velit aliquet sagittis id consectetur purus. Non sodales neque sodales ut etiam. Eget nunc lobortis mattis aliquam. Egestas erat imperdiet sed euismod nisi porta. Amet nulla facilisi morbi tempus iaculis. Tempus egestas sed sed risus pretium quam. Maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. Pulvinar sapien et ligula ullamcorper malesuada proin libero. Eget nulla facilisi etiam dignissim diam. Vulputate ut pharetra sit amet aliquam. Ultrices vitae auctor eu augue ut lectus arcu.

Feugiat nibh sed pulvinar proin gravida hendrerit lectus. Pellentesque sit amet porttitor eget dolor morbi non arcu risus. In hac habitasse platea dictumst quisque sagittis purus sit. Quis ipsum suspendisse ultrices gravida dictum fusce ut placerat. Duis tristique sollicitudin nibh sit. In dictum non consectetur a erat. Pulvinar sapien et ligula ullamcorper malesuada proin. Neque laoreet suspendisse interdum consectetur libero. Dolor morbi non arcu risus quis varius quam quisque. Donec adipiscing tristique risus nec. Tristique nulla aliquet enim tortor. Ultricies mi quis hendrerit dolor magna eget est lorem ipsum. Egestas diam in arcu cursus euismod quis. Sit amet nisl suscipit adipiscing bibendum est. Quis enim lobortis scelerisque fermentum dui faucibus in.
''')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_account, email_pass)
	
	smtp.send_message(msg)
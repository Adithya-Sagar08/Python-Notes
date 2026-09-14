import smtplib
from email.message import EmailMessage

# Email details
sendermailid = "adithyasagar502@gmail.com"
receivermailid = "adithyasagarrangapuram@gmail.com"
apppassword = "gblo sfny yjgz qjog"

# Email content
subject = "Birthday Invitation on 18th October 2026"
body = """
Good Morning, Ravi

I hope you are doing well,
I would hearty like to invite you to my birthday,
You should attend the birthday party without fail,
while coming to my birthday, don't forget to bring my gift 

Thanks and regards
Adithya Sagar
"""

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sendermailid
msg['To'] = receivermailid
msg.set_content(body)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sendermailid, apppassword)
        smtp.send_message(msg)
        print("Email has been sent successfully")
except Exception as e:
    print("Exception is:", e)
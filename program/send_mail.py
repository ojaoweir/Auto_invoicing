import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_invoice(template, password, subject):
    s=smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('codebuddyinfo@gmail.com', 'tddd83grupp9')


    sender = "ojaoweir@gmail.com"
    receiver = "ojaoweir@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    content = MIMEText(template, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(content)

    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()
    #end email setup

import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_invoice():
    s=smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('codebuddyinfo@gmail.com', 'tddd83grupp9')


    sender = "ojaoweir@gmail.com"
    receiver = "ojaoweir@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'invoice'
    msg['From'] = sender
    msg['To'] = receiver

    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)

    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()
    #end email setup

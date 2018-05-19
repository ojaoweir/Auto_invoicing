import smtplib
from program.db_functions import dbGetInvoice, dbGetSenderNameFromInvoice
from program.rendering import generateInvoiceTemplate
from program.general_functions import waitEnter, newLine
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def resendMailInvoice(id, password):
    server = startServer(password)
    invoice = dbGetInvoice(id)
    template = generateInvoiceTemplate(invoice)
    # TODO: FIX BELOW SO IT IS DYNAMIC
    sender = "ojaoweir@gmail.com"
    receiver = "ojaoweir@gmail.com"
    subject = 'Ny faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id: #' + str(invoice.id) + '#'
    sendMail(template, subject, sender, receiver, server)
    closeServer(server)
    newLine()
    print("Följande faktura har skickats om:")
    print(invoice)
    waitEnter()

def sendInvoices(invoices, password):
    server = startServer(password)
    # TODO: FIX BELOW SO IT IS DYNAMIC
    sender = "ojaoweir@gmail.com"
    receiver = "ojaoweir@gmail.com"
    for invoice in invoices:
        invoice = dbGetInvoice(invoice.id)
        template = generateInvoiceTemplate(invoice)
        subject = 'Ny faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id: #' + str(invoice.id) + '#'
        sendMail(template, subject, sender, receiver, server)
    # Terminate the SMTP session and close the connection

    closeServer(server)
    #end email setup

def closeServer(server):
    server.quit()

def startServer(password):
    server =smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login('codebuddyinfo@gmail.com', 'tddd83grupp9')
    return server

def sendMail(template, subject, sender, receiver, server):


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    content = MIMEText(template, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(content)

    server.send_message(msg)
    del msg

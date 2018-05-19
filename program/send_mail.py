import smtplib
from program.db_functions import dbGetInvoice, dbGetSenderNameFromInvoice, dbGetMainSenderEmail, dbGetCustomerEmailFromInvoice, dbGetSenderEmailFromInvoice
from program.rendering import generateInvoiceTemplate
from program.general_functions import waitEnter, newLine, drawLine
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def resendMailInvoice(id, password):
    server = startServer(password)
    invoice = dbGetInvoice(id)
    template = generateInvoiceTemplate(invoice)
    # TODO: FIX BELOW SO IT IS DYNAMIC
    sender = dbGetSenderEmailFromInvoice(invoice.id)
    receiver = dbGetCustomerEmailFromInvoice(invoice.id)
    subject = 'Ny faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id: #' + str(invoice.id) + '#'
    sendMail(template, subject, sender, receiver, server)
    closeServer(server)
    newLine()
    print("Följande faktura har skickats om:")
    print(invoice)
    waitEnter()

def sendInvoices(invoices, password, server):
    # TODO: FIX BELOW SO IT IS DYNAMIC
    sender = dbGetMainSenderEmail()
    for invoice in invoices:
        invoice = dbGetInvoice(invoice.id)
        template = generateInvoiceTemplate(invoice)
        receiver = dbGetCustomerEmailFromInvoice(invoice.id)
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
    try:
        server.login('codebuddyinfo@gmail.com', password)
    except Exception as error:
        newLine()
        drawLine()
        print("Nekad inlogging.\nFel lösenord eller ditt konto ej tillåter inlogg.\nFörsök igen...")
        drawLine()
        sys.exit(1)
    return server

def sendMail(template, subject, sender, receiver, server):


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg['cc'] = 'ojaoweir@gmail.com'

    content = MIMEText(template, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(content)

    server.send_message(msg)
    del msg

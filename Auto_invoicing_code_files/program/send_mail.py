import smtplib
from program.db_functions import dbGetInvoice, dbGetSenderNameFromInvoice, dbGetMainSenderEmail, dbGetCustomerEmailFromInvoice, dbGetSenderEmailFromInvoice
from program.rendering import generateInvoiceTemplate
from program.general_functions import waitEnter, newLine, drawLine
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, time

# resends the invoice with given id
def resendMailInvoice(id, password):
    newLine()
    print("Skickar fakturor...")
    # generating the invoice
    invoice = dbGetInvoice(id)
    template = generateInvoiceTemplate(invoice)
    sender = dbGetSenderEmailFromInvoice(invoice.id)
    # sets up server
    server = startServer(sender, password)
    receiver = dbGetCustomerEmailFromInvoice(invoice.id)
    subject = 'Omskickad faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id #' + str(invoice.id) + '#'
    # sends the mail and closes the connection
    sendMail(template, subject, sender, receiver, server)
    closeServer(server)
    # prints a confirmation
    newLine()
    print("Följande faktura har skickats om:")
    print(invoice)
    waitEnter()

def sendInvoices(invoices, password, server):
    newLine()
    print("Skickar fakturor...")
    sender = dbGetMainSenderEmail()
    for invoice in invoices:
        # generating the invoice
        invoice = dbGetInvoice(invoice.id)
        template = generateInvoiceTemplate(invoice)
        receiver = dbGetCustomerEmailFromInvoice(invoice.id)
        subject = 'Ny faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id: #' + str(invoice.id) + '#'
        sendMail(template, subject, sender, receiver, server)
    # Closes the server connection
    closeServer(server)

# function to close server connection
def closeServer(server):
    server.quit()

# function to add server connection
# Only works with gmail
# gmail account has to have 'allow unsecure apps' turned on
def startServer(email, password):
    server =smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    try:
        server.login(email, password)
    except Exception as error:
        # shows an error in case logging in fails
        newLine()
        drawLine()
        print("Nekad inlogging.\nFel lösenord eller ditt konto ej tillåter inlogg.\nFörsök igen...")
        drawLine()
        time.sleep(2)
        sys.exit(1)
    return server

# sends an mail with the details imported
def sendMail(template, subject, sender, receiver, server):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg['Cc'] = 'ojaoweir@gmail.com'

    # Attaches template to mail
    content = MIMEText(template, 'html')
    msg.attach(content)
    # sends the mail
    server.send_message(msg)
    del msg

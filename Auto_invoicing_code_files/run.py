from program import app, db
from program.get_data import getCustomer, getServices, getPassword, printSendConfirmation
from program.db_functions import dbRemoveOldInvoices, dbCreateAndGetInvoice, dbGetInvoice, dbGetSenderNameFromInvoice, dbGetSender, dbGetMainSender
from program.send_mail import sendInvoices, startServer

# Gets input of all customers getting the invoices
customers = getCustomer()
# The following will set up the connection to the mail server
main_sender_mail = dbGetSender(dbGetMainSender()).email
password = getPassword(main_sender_mail)
server = startServer(main_sender_mail, password)
# Creates a invoice for every customer
invoices = dbCreateAndGetInvoice(customers)
dbRemoveOldInvoices()
getServices(invoices)
# Sends all invoices through the mail service
sendInvoices(invoices, password, server)
# Prints a confirmation that the invoice has been sent
printSendConfirmation(invoices)

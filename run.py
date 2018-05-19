from program import app, db
from program.get_data import getCustomer, getServices, getPassword, printSendConfirmation
from program.db_functions import dbCreateAndGetInvoice, dbGetInvoice, dbGetSenderNameFromInvoice, dbGetSender, dbGetMainSender
from program.send_mail import sendInvoices, startServer

customers = getCustomer()
main_sender_mail = dbGetSender(dbGetMainSender()).email
password = getPassword(main_sender_mail)
server = startServer(main_sender_mail, password)
invoices = dbCreateAndGetInvoice(customers)
getServices(invoices)
sendInvoices(invoices, password, server)
printSendConfirmation(invoices)

from program import app, db
from program.get_data import getCustomer, getServices, getPassword, printSendConfirmation
from program.db_functions import dbCreateAndGetInvoice, dbGetInvoice, dbGetSenderNameFromInvoice, dbGetSender, dbGetMainSender
from program.send_mail import sendInvoices, startServer

customers = getCustomer()
password = getPassword(dbGetSender(dbGetMainSender()).email)
server = startServer(password)
invoices = dbCreateAndGetInvoice(customers)
getServices(invoices)
sendInvoices(invoices, password, server)
printSendConfirmation(invoices)

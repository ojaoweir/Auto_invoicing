from program import app, db
from program.get_data import getCustomer, getServices, getPassword
from program.db_functions import dbCreateAndGetInvoice, dbGetInvoice, dbGetSenderNameFromInvoice, dbGetSender, dbGetMainSender
from program.send_mail import sendInvoices

customers = getCustomer()
invoices = dbCreateAndGetInvoice(customers)
getServices(invoices)
password = getPassword(dbGetSender(dbGetMainSender()).email)
sendInvoices(invoices, password)

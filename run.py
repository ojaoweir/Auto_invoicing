from program import app, db
from program.get_data import getCustomer, getServices, getPassword
from program.db_functions import dbCreateAndGetInvoice, dbGetInvoice, dbGetSenderNameFromInvoice
from program.rendering import generateInvoiceTemplate
from program.send_mail import send_invoice

customer = getCustomer()
invoice = dbCreateAndGetInvoice(customer)
getServices(invoice)
invoice = dbGetInvoice(invoice.id)
password = getPassword()
template = generateInvoiceTemplate(invoice)
subject = 'Ny faktura från ' + dbGetSenderNameFromInvoice(invoice.id) + ', id: #' + str(invoice.id) + '#'
send_invoice(template, password, subject)

from program import app, db
from program.get_data import getCustomer, getServices, getPassword
from program.db_functions import dbCreateAndGetInvoice
from program.rendering import generateInvoiceTemplate
from program.send_mail import send_invoice

customer = getCustomer()
invoice = dbCreateAndGetInvoice(customer)
getServices(invoice)
password = getPassword()
template = generateInvoiceTemplate(invoice)
send_invoice(template, password)

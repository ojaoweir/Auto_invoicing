from program import app, db
from program.get_data import getCustomer, getServices
from program.db_functions import dbCreateAndGetInvoice

customer = getCustomer()
invoice = dbCreateAndGetInvoice(customer)
getServices(invoice)

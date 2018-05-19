from flask import url_for
from program import app, db
from jinja2 import Environment, FileSystemLoader
from program.models import Invoice, Sender, Customer
from program.db_functions import dbGetSender, dbGetCustomer

# function to render an invoice template from data entered
def generateInvoiceTemplate(invoice):
    sender = dbGetSender(invoice.sender_id)
    customer = dbGetCustomer(invoice.customer_id)
    services = invoice.payed_service
    total_price_for_all = invoice.price
    invoice_date = invoice.getDate()
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("program/templates/invoice.html")
    # below is defining the data so that the template can read it
    template_variables = {"sender": sender,
                        "customer": customer,
                        "invoice": invoice,
                        "services":services,
                        "total_price_for_all": total_price_for_all,
                        "invoice_date": invoice_date}
    return template.render(template_variables)

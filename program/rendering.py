from flask import url_for
from program import app, db
from jinja2 import Environment, FileSystemLoader
from program.models import Invoice, Sender, Customer
from program.db_functions import dbGetSender, dbGetCustomer

def generateInvoiceTemplate(invoice):
    sender = dbGetSender(invoice.sender_id)
    customer = dbGetCustomer(invoice.customer_id)
    services = invoice.payed_service
    total_price_for_all = invoice.price
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("program/templates/invoice.html")
    template_variables = {"sender": sender,
                        "customer": customer,
                        "invoice": invoice,
                        "services":services,
                        "total_price_for_all": total_price_for_all}
    return template.render(template_variables)

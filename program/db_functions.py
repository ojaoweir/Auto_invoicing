from .models import Customer, Invoice, Service, Sender
from program import db


def dbAddCustomer(name, address, city, country, email):
    c = Customer(name = name, address = address, city = city, country = country, email = email)
    db.session.add(c)
    db.session.commit()
    return c

def dbGetInvoice(id):
    return Invoice.query.get(id)

def dbGetAllCustomers():
    return Customer.query.all()

def dbGetCustomer(id):
    return Customer.query.get(id)

def dbGetSender(id):
    return Sender.query.get(id)

def dbGetMainSender():
    return Sender.query.filter_by(is_main=True).first().id

def dbCreateAndGetInvoice(customer):
    i = Invoice(customer_id = customer.id, sender_id = dbGetMainSender())
    db.session.add(i)
    db.session.commit()
    return i

def dbAddService(service_name, amount, price_per, invoice):
    s = Service(service_name = service_name, price_per = price_per,
                price_total = price_per*float(amount), amount = amount, invoice_id = invoice.id)
    db.session.add(s)
    db.session.commit()

def dbCommit():
    db.session.commit()

def dbCalculateInvoicePrice(invoice):
    Invoice.query.get(invoice.id).setPrice()
    dbCommit()

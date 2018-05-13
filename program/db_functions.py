from .models import Customer, Invoice, Service
from program import db


def dbAddCustomer(name, address, city, country, email):
    c = Customer(name = name, address = address, city = city, country = country, email = email)
    db.session.add(c)
    db.session.commit()
    return c

def dbGetAllCustomers():
    return Customer.query.all()

def dbGetCustomer(id):
    return Customer.query.get(id)

def dbCreateAndGetInvoice(customer):
    i = Invoice(customer_id = customer.id)
    db.session.add(i)
    db.session.commit()
    return i

def dbAddService(service_name, amount, price_per, invoice):
    s = Service(service_name = service_name, price_per = price_per,
                price_total = price_per*float(amount), amount = amount, invoice_id = invoice.id)
    db.session.add(s)

def dbCommit():
    db.session.commit()

def dbCalculateInvoicePrice(invoice):
    invoice.setPrice()
    dbCommit()

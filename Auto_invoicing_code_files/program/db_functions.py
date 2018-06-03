from .models import Customer, Invoice, Service, Sender
from program import db
from sqlalchemy import func

def dbGetAllInvoices():
    return Invoice.query.all()

# creates a new customer in database
def dbAddCustomer(name, address, city, country, email):
    c = Customer(name = name, address = address, city = city, country = country, email = email)
    db.session.add(c)
    db.session.commit()

def dbGetInvoice(id):
    return Invoice.query.get(id)

def dbGetAllCustomers():
    return Customer.query.all()

def dbGetAllSenders():
    return Sender.query.all()

# Changes which sender from which new invoices will be sent From
# resent invoices will be sent from their original sender
def dbChangeMain(new_main):
    old_main = dbGetMainSender()
    dbGetSender(old_main).remove_main()
    dbGetSender(new_main).set_main()
    db.session.commit()

def dbGetCustomer(id):
    return Customer.query.get(id)

def dbGetSender(id):
    return Sender.query.get(id)

# creates a new sender in database
def dbAddSender(name, address, city, zip_code, country, email, phone_number, organisation_number, payment_method,account_number, complaint_link, logo_link):
    s = Sender(name=name, address=address, city=city, organisation_number=organisation_number, zip_code=zip_code, country=country, email=email, phone_number=phone_number, payment_method=payment_method,account_number=account_number, complaint_link = complaint_link, logo_link = logo_link)
    db.session.add(s)
    db.session.commit()

def dbGetMainSender():
    return Sender.query.filter_by(is_main=True).first().id

def dbGetMainSenderEmail():
    return Sender.query.filter_by(is_main=True).first().email

# The function below deletes old invoice so no to get overflow in database
def dbRemoveOldInvoices():
    limit = Invoice.query.order_by(Invoice.id.desc()).first().id - 25
    print(limit)
    Invoice.query.filter(Invoice.id <= limit).delete()
    db.session.commit()

# creates a new invoice in database
def dbCreateAndGetInvoice(customers):
    invoices = []
    for customer in customers:
        invoice = Invoice(customer_id = customer.id, sender_id = dbGetMainSender())
        db.session.add(invoice)
        invoices.append(invoice)
    db.session.commit()
    return invoices

# creates new services connected to given invoice
def dbAddService(service_name, amount, price_per, invoice):
    s = Service(service_name = service_name, price_per = price_per,
                price_total = price_per*float(amount), amount = amount, invoice_id = invoice.id)
    db.session.add(s)
    db.session.commit()

def dbCommit():
    db.session.commit()

# updates the total price on an invoice
def dbCalculateInvoicePrice(invoice):
    Invoice.query.get(invoice.id).setPrice()
    dbCommit()

def dbGetSenderNameFromInvoice(id):
    sender_id = dbGetInvoice(id).sender_id
    return dbGetSender(sender_id).name

def dbGetSenderEmailFromInvoice(id):
    sender_id = dbGetInvoice(id).sender_id
    return dbGetSender(sender_id).email

def dbGetCustomerEmailFromInvoice(id):
    receiver_id = dbGetInvoice(id).customer_id
    return dbGetCustomer(receiver_id).email

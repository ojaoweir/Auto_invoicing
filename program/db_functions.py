from .models import Customer
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

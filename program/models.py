from program import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index = True, nullable = False)
    address = db.Column(db.String(64), index =True, nullable = True)
    city = db.Column(db.String(32), index = True, nullable = True)
    country = db.Column(db.String(32), index = True, nullable = True)
    email = db.Column(db.String(64), index = True, nullable = False)

    def __repr__(self):
        return 'ID:{}\n{}, {}'.format(self.id, self.name, self.email)

class Sender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index = True, nullable = False)
    address = db.Column(db.String(64), index =True, nullable = False)
    city = db.Column(db.String(32), index = True, nullable = False)
    country = db.Column(db.String(32), index = True, nullable = False)
    email = db.Column(db.String(64), index = True, nullable = False)
    zip_code = db.Column(db.Integer, nullable = False)
    organisation_number = db.Column(db.String(16), index = True, nullable = False)
    phone_number = db.Column(db.String(16), index = True, nullable = False)
    account_number = db.Column(db.String(16), index = True, nullable = False)
    payment_method = db.Column(db.String(16), index = True, nullable = False)
    complaint_link = db.Column(db.String(86), index = True, nullable = False)
    logo_link = db.Column(db.String(86), index = True, nullable = False)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    service_name = db.Column(db.String(32), index = True, nullable = False)
    price_per = db.Column(db.Float, nullable = False)
    price_total = db.Column(db.Float, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable = False)

    invoice = db.relationship("Invoice", backref="invoice_for_service", foreign_keys = [invoice_id])


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, index = True, default = datetime.now)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    payed_service = db.relationship("Service", primaryjoin=id==Service.invoice_id)

    def setPrice(self):
        price = 0
        for service in self.payed_service:
            price = price + service.price_total
        self.price = price

from program import db
from datetime import datetime
from sqlalchemy import Date, cast

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index = True, nullable = False)
    address = db.Column(db.String(64), index =True, nullable = True)
    city = db.Column(db.String(32), index = True, nullable = True)
    country = db.Column(db.String(32), index = True, nullable = True)
    email = db.Column(db.String(64), index = True, nullable = False)

    def __repr__(self):
        return 'ID:{} \n{} \n {}'.format(self.id, self.name, self.email)

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
    complaint_link = db.Column(db.String(86), index = True, nullable = False, default = "https://i.imgur.com/JfHjOEP.jpg")
    logo_link = db.Column(db.String(86), index = True, nullable = False)
    is_main = db.Column(db.Boolean, default = False)

    def set_main(self):
        self.is_main = True

    def remove_main(self):
        self.is_main = False

    def __repr__(self):
        return 'ID:{}\n {} \n {} \n {}: {} \n Main:{}'.format(self.id, self.name, self.email, self.payment_method, self.account_number, self.is_main)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    service_name = db.Column(db.String(32), index = True, nullable = False)
    price_per = db.Column(db.Float, nullable = False)
    price_total = db.Column(db.Float, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable = False)

    invoice = db.relationship("Invoice", backref="invoice_for_service", foreign_keys = [invoice_id])

    def __repr__(self):
        return '{}st {} {}kr tot'.format(self.amount, self.service_name, self.price_total)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, index = True, default = datetime.now)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable = False)
    sender_id = db.Column(db.Integer, db.ForeignKey('sender.id'), nullable = False)

    payed_service = db.relationship("Service", primaryjoin=id==Service.invoice_id)

    def __repr__(self):
        return 'ID:{}\nmottagare:{}\ndatum:{}\npris:{}\n{}'.format(self.id, self.customer_id, self.date, self.price, self.payed_service)

    def setPrice(self):
        price = 0
        for service in self.payed_service:
            price = price + service.price_total
        self.price = price

    def getDate(self):
        return self.date.date()

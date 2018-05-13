from flask import render_template
from program import app, db

def generateInvoiceTemplate(invoice):
    return render_template('invoice.html')

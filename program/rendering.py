from flask import render_template
from program import app, db
from jinja2 import Environment, FileSystemLoader

def generateInvoiceTemplate(invoice):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("program/invoice.html")
    return template

# from weasyprint import HTML
from xthml2pdf import pisa
from .rendering import render_invoice

sourceHtml = "<html><head lang='en'><meta charset='UTF-8'><title>test1</title></head><body><h2>test2</h2>test3</body></html>"
html_out = render_invoice()
HTML(string=html_out).write_pdf("report.pdf")

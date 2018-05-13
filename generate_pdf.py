from weasyprint import HTML
from rendering import render_invoice

html_out = render_invoice()
HTML(string=html_out).write_pdf("report.pdf")

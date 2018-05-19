from .db_functions import *
from .general_functions import drawLine, newLine, waitEnter
from getpass import getpass
from .send_mail import resendMailInvoice

def getCustomer():
    newLine()
    drawLine()
    print('VÄLJ MOTTAGARE')
    drawLine()
    choice = input("Ange id till en eller flera mottagare (separera med space): \n (0 för att se lista, 'XXX' för adminview)\n")
    if (choice == '0'):
        return printAllCustomers()
    elif (choice == 'XXX'):
        customers = adminView()
    else:
        customers = separateCustomers(choice)
        for customer in customers:
            newLine()
            print("Du har valt person " + str(customer.id) + ":")
            print(customer)
            drawLine()
    return customers

def enterNewCustomer():
    newLine()
    drawLine()
    print('SKAPA NY MOTTAGARE')
    drawLine()
    name = input("Ange namn: ")
    address = input("Ange address: ")
    city = input("Ange stad: ")
    country = input("Ange land: ")
    email = input("Ange email: ")
    dbAddCustomer(name, address, city, country, email)

def printAllCustomers():
    newLine()
    drawLine()
    print('ALLA SPARADE MOTTAGARE')
    drawLine()
    customers = dbGetAllCustomers()
    for customer in customers:
        newLine()
        print(customer)
    drawLine()
    newLine()
    waitEnter()
    return getCustomer()

def printAllSenders():
    newLine()
    drawLine()
    print('ALLA SPARADE SKICKARE')
    drawLine()
    senders = dbGetAllSenders()
    for sender in senders:
        newLine()
        print(sender)
    drawLine()
    newLine()
    waitEnter()

def printAllInvoices():
    newLine()
    drawLine()
    print('ALLA FAKTUROR')
    drawLine()
    invoices = dbGetAllInvoices()
    for invoice in invoices:
        newLine()
        print(invoice)
    drawLine()
    newLine()
    waitEnter()

def getServices(invoices):
    services = []
    nr_of_services = int(input("Ange hur många artiklar:"))
    for i in range(0,nr_of_services):
        newLine()
        drawLine()
        getAndAddService(invoices)
    for invoice in invoices:
        dbCalculateInvoicePrice(invoice)

def getAndAddService(invoices):
    service_name = input("Ange namn på artikel: ")
    amount = int(input("Ange hur många av denna artikel: "))
    price_per = float(input("Ange pris per enhet: "))
    for invoice in invoices:
        dbAddService(service_name, amount, price_per, invoice)

def getPassword(sender_mail):
    print("Ange ditt password till " + sender_mail + ":")
    password = getpass()
    return password

def changeMainSender():
    sender_id = int(input("Ange vilken sender du vill ska bli nya main:"))
    dbChangeMain(sender_id)
    print("Ny main sender är:")
    print(dbGetSender(dbGetMainSender()))
    waitEnter()

def enterNewSender():
    newLine()
    drawLine()
    print('SKAPA NY SENDER')
    drawLine()
    name = input("Ange namn: ")
    address = input("Ange address: ")
    city = input("Ange stad: ")
    zip_code = input("Ange postkod: ")
    country = input("Ange land: ")
    email = input("Ange email: ")
    organisation_number = input("Ange organisationsnummer: ")
    phone_number = input("Ange telefonnummer: ")
    payment_method = input("Ange betalsätt: ")
    account_number = input("Ange kontonummer: ")
    logo_link = input("Ange länk till logotyp: ")
    complaint_link = input("Ange länk för klagomål: ")
    dbAddSender(name, address, city, zip_code, country, email, phone_number, organisation_number, payment_method,account_number, complaint_link, logo_link)


def adminView():
    newLine()
    drawLine()
    print('ADMINVIEW')
    drawLine()
    choice = input("Ange vad du vill göra:\n(0 - skapa ny kund, 1 - se lista av senders, 2 - byt sender, 3 - skapa ny sender, 4 - skicka om faktura, 5 - lämna adminView)\n")
    if (choice == '0'):
        enterNewCustomer()
    elif (choice == '1'):
        printAllSenders()
    elif (choice == '2'):
        changeMainSender()
    elif (choice == '3'):
        enterNewSender()
    elif (choice == '4'):
        resendInvoice()
    elif (choice == '5'):
        return getCustomer()
    else:
        print("felaktig input")
        return adminView()


def resendInvoice():
    choice = input("Ange id på den faktura du vill skicka igen: \n(0 för att se alla)\n")
    if (choice == '0'):
        printAllInvoices()
        resendInvoice()
    else:
        password = getPassword(dbGetSenderEmailFromInvoice(int(choice)))
        resendMailInvoice(int(choice), password)

def separateCustomers(input):
    input_customer = ''
    customers = []
    for char in input:
        if not char == ' ':
            input_customer = input_customer + char
        else:
            customers.append(dbGetCustomer(int(input_customer)))
            input_customer = ''
    customers.append(dbGetCustomer(int(input_customer)))
    return customers

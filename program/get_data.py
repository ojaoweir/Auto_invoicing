from .db_functions import dbAddCustomer, dbGetAllCustomers, dbGetCustomer
from .general_functions import drawLine, newLine, waitEnter

def getCustomer():
    newLine()
    drawLine()
    print('VÄLJ MOTTAGARE')
    drawLine()
    choice = input("Ange id till mottagare: (0 för att se lista, - för att skapa ny)")
    if (choice == '0'):
        return printAllCustomers()
    elif (choice == '-'):
        customer = enterNewCustomer()
    else:
        newLine()
        customer = dbGetCustomer(choice)
        print("Du har valt person " + choice + ":")
        print(customer)
        drawLine()
    return customer

def enterNewCustomer():
    newLine()
    drawLine()
    print('Skapa ny kund')
    drawLine()
    name = input("Ange namn: ")
    address = input("Ange address: ")
    city = input("Ange stad: ")
    country = input("Ange land: ")
    email = input("Ange email: ")
    return dbAddCustomer(name, address, city, country, email)

def printAllCustomers():
    newLine()
    drawLine()
    print('ALLA SPARADE MOTTAGARE')
    drawLine()
    customers = dbGetAllCustomers()
    for customer in customers:
        print(customer)
    drawLine()
    newLine()
    waitEnter()
    return getCustomer()

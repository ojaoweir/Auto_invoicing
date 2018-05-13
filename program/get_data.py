from .db_functions import dbAddCustomer, dbGetAllCustomers, dbGetCustomer
from .general_functions import drawLine

def getCustomer():
    choice = input("Ange id till mottagare: (0 för att se lista, - för att skapa ny)")
    if (choice == '0'):
        return printAllCustomers()
    elif (choice == '-'):
        customer = enterNewCustomer()
    else:
        customer = dbGetCustomer(choice)
        print("Du har valt person " + choice + ":")
        print(customer)
    return customer

def enterNewCustomer():
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
    customers = dbGetAllCustomers()
    for customer in customers:
        print(customer)
    return getCustomer()

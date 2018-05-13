def getCustomer():
    choice = input("Ange id till mottagare: (0 för att se lista, - för att skapa ny)")
    if (choice == '0'):
        print("här ska alla skriva ut")
    elif (choice == '-'):
        print("skapa ny")
    else:
        print("Du har valt person " + choice)

def enterNewCustomer():
    print('Skapa ny kund')
    name = input("Ange namn: ")
    address = input("Ange address: ")
    city = input("Ange stad: ")
    country = input("Ange land: ")
    email = input("Ange email: ")
    dbAddCustomer(name, address, city, country, email)
    

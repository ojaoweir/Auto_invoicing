def dbAddCustomer(name, address, city, country, email):
    c = Customer(name = name, address = address, city = city, country = country, email = email)
    db.session.add(c)
    db.session.commit()

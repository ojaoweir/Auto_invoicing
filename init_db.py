from program import db

#Run this script with the command "python init_db.py" to initialize (restore) the database.

def initialize_database():
	db.reflect()
	db.drop_all()
	db.create_all()


if __name__ == '__main__':
    initialize_database()

# adding the basic sender that will always be there
from program.models import Sender

s = Sender(name = 'Irre-Snirre Fixar', address = 'Tröskaregatan 65', city = 'Linköping', country = 'Sverige',
            email = 'ojaoweir@gmail.com', zip_code=58333, organisation_number='961002-2858',
            phone_number = '070-7795557', account_number = '070-7795557', payment_method = 'Swish',
            complaint_link = 'https://i.imgur.com/JfHjOEP.jpg', logo_link = 'https://i.imgur.com/TtkQXrw.png')

db.session.add(s)
db.session.commit()

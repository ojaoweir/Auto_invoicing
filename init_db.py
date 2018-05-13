from program import db

#Run this script with the command "python init_db.py" to initialize (restore) the database.

def initialize_database():
	db.reflect()
	db.drop_all()
	db.create_all()


if __name__ == '__main__':
    initialize_database()

s = se

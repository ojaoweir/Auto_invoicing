#Configuration class to separe config-choices from the rest of the application
import os

basedir = os.path.abspath(os.path.dirname(__file__))

#The setting are defines as class variables inside the Config-class
class Config(object):
    #Important! Cryptographic key, protects the app from CSRF attacks
    #First term looks for the value of an environment variable "SECRET_KEY"
    #Second term is a hardcoded string, can be used if SECRET_KEY isnt found
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True;

    BASIC_AUTH_USERNAME = 'group9'
    BASIC_AUTH_PASSWORD = 'password'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #Signals the application everytime a change is made in the database when True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

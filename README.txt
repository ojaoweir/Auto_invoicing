Auto_invoicing
Python 3 is required to run this program

to abort anytime press ctrl+c

This program only works for sending from google emails
  Access for less secure apps needs to be turned on for sender emails
  The program will always send a copy to 'ojaoweir@gmail.com'

For first time run the 'setup.bat' file (takes a while, be patient)
  If that does not work do the following

    If there is not a virtual environment (a folder called 'venv')
      Start a virtual environment
        python -m venv venv

    Source that virtual environment
      source venv/bin/activate (linux/mac)
      venv\Scripts\activate (windows)

    Install packages included in requirements.txt
      pip install -r requirement.txt  
        (I had to upgrade setuptools for weasyprint to work 'pip install --upgrade setuptools')


To start the app run the launch_application.bat
  if that does not work do following
  enter the folder "Auto_invoicing"
    start cmd here
      enter python run.py

To enter new customer, account to send from, or change account to send from enter adminView

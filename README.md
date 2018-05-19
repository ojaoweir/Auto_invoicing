Auto_invoicing

Python is required to run this program
This program only works for google emails

Password for snirrfakturor : "IrrSnirr96"

For first time run the setup.bat file. If that does not work, do the following

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
  enter the folder "application"
    start cmd here
      enter python run.py

To enter new customer, account to send from, or change account to send from enter adminView

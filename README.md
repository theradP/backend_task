The Home-Automation Controller Template
I made this project as a task for an interview. In this project user can add a device to the network, remove a device 
from the network, list all devices added and make the added device do a task.
The api stores data regarding all tasks done by devices that are added to the network.

Pre-requisites
-Python 3.6
-Postman (for viewing documentation)

Getting started 
-First create a virtual environment either using conda or virtualenv
-run command 'pip install -r requirements.txt' to install all dependencies
-As migration files and db are added in the repo just run 'python manage.py runserver' to initiate the project server.
If any issues related to database are faced just remove the migration files and run 'python manage.py makemigrations' 
then 'python manage.py migrate' and then run the server

Tech Stack
-Python - Language of choice
-pip - package manager
-Django - webapp framework
-djangorestframework - REST framework for Django
-SQLlite3 - Database used in the project

Documentation - https://documenter.getpostman.com/view/10412699/SzKPX2Jj

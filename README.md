## Hello service

In this service you can input a name, and get a "Hello" response, if name 
not in DB or get 'you were already here' response, if this name in DB.

The service has two pages: a form for input the name and list of names from DB.

This project use clearer SQLlite database


### installation

download repository

- installing dependencies
Open a console in the current folder and enter:
```sh
python3 -m venv myvenv
C:<path to directory> myvenv \ Scripts \ activate
pip install requirements.txt
```
or
```sh
pipenv install
```
after successful installation, to run the program, type in the console
```sh
python manage.py runserver
python manage.py createsuperuser
```

open a browser and go to ``` http://localhost:8000/```

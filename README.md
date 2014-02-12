What this is for
================

Setup a django project and first app with a few favorite 3rd party apps already installed

How to install
--------------

cd ~/sites\n
mkdir project-name\n
mkdir project-name/virtualenv\n
mkdir project-name/database\n
mkdir project-name/source\n

git clone https://github.com/bjdixon/django-initial-setup.git ~/sites/project-name/source

virtualenv -p python3 ./virtualenv

source ./virtualenv/bin/activate

cd source

pip install -r requirements.txt

python3 manage.py runserver

Includes
--------

South
Selenium
Gunicorn
Bootstrap (in sample app)


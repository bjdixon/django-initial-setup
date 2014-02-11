What this is for
================

Setup a django project and first app with a few favorite 3rd party apps already installed

How to install
==============

cd ~/sites
mkdir project-name
mkdir project-name/virtualenv
mkdir project-name/database
mkdir project-name/source

git clone https://github.com/bjdixon/django-initial-setup.git ~/sites/project-name/source

virtualenv -p python3 ./virtualenv

source ./virtualenv/bin/activate

cd source

pip install -r requirements.txt

python3 manage.py runserver


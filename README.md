What this is for
================

Setup a django project and first app with a few favorite 3rd party apps already installed

How to install
--------------

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

Rename project_name and app_name  
-----------------------------------------------
mv project_name/ new_project_name/  
mv app_name/ new_app_name/  

find . -type f -print0 | xargs -0 sed -i 's/project_name/new_project_name/g'  
find . -type f -print0 | xargs -0 sed -i 's/app_name/new_app_name/g'  

Includes
--------

South  
Selenium  
Gunicorn  
Bootstrap (in sample app)  
django-braces  
django-simple-history  
pep8  
pyflakes  

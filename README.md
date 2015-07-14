# inventory_management

pip install virtualenvwrapper
mkvirtualenv env -r requirements.txt --python=/usr/bin/python3 #path to your python3 installation

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver

deactivate
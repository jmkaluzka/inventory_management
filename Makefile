PROJECT = inventory
ENV = inv

all: run

install: migrate
	#pip install virtualenvwrapper
	#which virtualenvwrapper.sh
	#source /usr/local/bin/virtualenvwrapper.sh
	#mkvirtualenv $(ENV)
	#mkvirtualenv inv -r requirements.txt --python=/usr/bin/python3
	#pip install -r requirements.txt
	#migrate
	python manage.py createsuperuser --username admin --email empty

migrate:
	python manage.py makemigrations
	python manage.py migrate

orm:
	python manage.py shell

run:
	python manage.py runserver


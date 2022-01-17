#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:8010
#gunicorn config.wsgi:application --bind 0.0.0.0:8010
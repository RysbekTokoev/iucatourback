#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

python manage.py runserver 192.168.200.15:8010
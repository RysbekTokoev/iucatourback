# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /IUCA_tour
WORKDIR /IUCA_tour
COPY ./IUCA_tour /IUCA_tour/

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./entrypoint.sh /

RUN python manage.py makemigrations
RUN python manage.py makemigrations main
RUN python manage.py migrate
ENTRYPOINT ["sh", "/entrypoint.sh"]
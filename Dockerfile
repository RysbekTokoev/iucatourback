FROM python:3

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./IUCA_tour /app
WORKDIR /app

# copy our project code
COPY . /opt/services/djangoapp/src

COPY ./entrypoint.sh /
RUN python manage.py makemigrations
RUN python manage.py makemigrations main

ENTRYPOINT ["sh", "/entrypoint.sh"]
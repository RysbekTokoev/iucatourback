FROM python:3

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./IUCA_tour /app
WORKDIR /app


COPY ./entrypoint.sh /
RUN python manage.py makemigrations
RUN python manage.py makemigrations main
RUN python manage.py migrate
ENTRYPOINT ["sh", "/entrypoint.sh"]
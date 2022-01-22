# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# arbitrary location choice
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "IUCA_tour", "--bind", ":8000", "config.wsgi:application"]

# pull official base image
FROM python:3

# set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn todoServe.wsgi:application --bind 0.0.0.0:$PORT
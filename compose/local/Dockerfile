FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3-virtualenv cron
RUN virtualenv venv
RUN /venv/bin/pip install -U pip
WORKDIR /app
COPY . /app
#RUN crontab /app/app/config/crontab
RUN /venv/bin/pip install -r /app/requirements.txt

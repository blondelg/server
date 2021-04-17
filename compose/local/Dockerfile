FROM ubuntu:20.04
ENV EMAIL_USERNAME=geoffroypointblondel@gmail.com
ENV EMAIL_PASSWORD=UM5B6dyVeudSgvND6xkL
RUN apt-get update
RUN apt-get install -y python3-virtualenv
RUN virtualenv venv
RUN /venv/bin/pip install -U pip
WORKDIR /app
COPY . /app
RUN /venv/bin/pip install -r /app/requirements.txt

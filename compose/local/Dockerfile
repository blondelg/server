FROM ubuntu:20.04
ENV EMAIL_USERNAME=geoffroypointblondel@gmail.com
ENV EMAIL_PASSWORD=geoffroypointblondel@gmail.com
RUN apt-get update
RUN apt-get install -y python3-virtualenv
RUN virtualenv venv
RUN /venv/bin/pip install -U pip
COPY . /
RUN /venv/bin/pip install -r /requirements.txt

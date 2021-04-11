FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3-virtualenv
RUN virtualenv venv
RUN /venv/bin/pip install -U pip
COPY . /
RUN /venv/bin/pip install -r /requirements.txt

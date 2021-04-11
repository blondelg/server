#!/bin/bash

apt-get update
apt-get install -y python3-virtualenv
virtualenv venv
venv/bin/pip install -U pip
venv/bin/pip install -r requirements.txt

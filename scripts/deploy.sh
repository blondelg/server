#!/bin/bash
git clone git@github.com:blondelg/server.git
apt-get update
apt-get install -y python3-virtualenv
virtualenv venv
venv/bin/pip install -U pip
venv/bin/pip install -r requirements.txt

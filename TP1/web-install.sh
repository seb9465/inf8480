#!/bin/bash

sudo apt-get update
sudo apt-get install -y -q python
sudo apt-get install -y -q python-pip
sudo apt-get install -y -q postgresql
sudo apt-get install libpq-dev
pip install psycopg2
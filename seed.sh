#!/bin/bash

# Load the fixtures data into the database
#
# Delete local database if exists
db=local_database.sqlite3
[[ -f "$db" ]] && rm local_database.sqlite3

# Makes migrations
python3 manage.py makemigrations

# Migrates databse
yes | python3 manage.py migrate


FIX_LOC='seeds/'

python3 manage.py loaddata "$FIX_LOC"department
python3 manage.py loaddata "$FIX_LOC"employee

echo "Cleanning pyc"
find . -name "*.pyc" -exec rm -rf {} \;


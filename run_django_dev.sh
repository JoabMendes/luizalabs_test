#!/usr/bin/env bash


find . -name "*.hot-update.*" -exec rm -rf {} \;
find . -name "*.pyc" -exec rm -rf {} \;
./manage.py runserver

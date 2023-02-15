#!/usr/bin/env bash

# exit on error
set -o errexit

pip install -r dependencies.txt

python manage.py migrate
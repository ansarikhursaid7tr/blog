#!/bin/bash

echo "Building project packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Migrating Database..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Build script completed successfully"

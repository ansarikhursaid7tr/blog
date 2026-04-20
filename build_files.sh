#!/bin/bash

echo "Building project packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt

echo "Building frontend assets..."
npm install
npm run build

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Build script completed successfully"

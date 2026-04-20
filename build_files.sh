#!/bin/bash

# Exit on any error
set -e

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Building project packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Building frontend assets..."
npm install
npm run build

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Build script completed successfully"

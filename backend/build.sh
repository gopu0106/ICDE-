#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Run seeding to ensure data is present
python seed.py

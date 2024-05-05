#!/bin/bash

echo "Apply Database Migrations"
python manage.py migrate

exec "$@"
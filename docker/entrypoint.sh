#!/bin/sh

set -e

python manage.py collectstatic --noinput # collect static files into one location for NGINX
python manage.py wait_for_postgres # wait for database to be ready
python manage.py migrate
python manage.py check --deploy
uwsgi --socket :8000 --master --enable-threads --module website.wsgi
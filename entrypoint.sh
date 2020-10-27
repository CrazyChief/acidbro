#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOSTNAME $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
# gunicorn acidbro.wsgi:application --bind 0.0.0.0:8000

exec "$@"

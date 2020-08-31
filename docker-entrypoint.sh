#!/bin/sh
set -e
python manage.py collectstatic --noinput

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

exec "$@"
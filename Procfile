release: python manage.py migrate
web: gunicorn -t 1200 certwebapp.wsgi:application --log-file -
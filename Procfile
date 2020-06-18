release: python manage.py migrate
worker: python manage.py process_tasks
web: gunicorn -t 1200 certwebapp.wsgi:application --log-file -
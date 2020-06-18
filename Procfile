release: python manage.py migrate
worker: python manage.py process_tasks
worker: python manage.py qcluster
web: gunicorn -t 1200 certwebapp.wsgi:application --log-file -
FROM python:3.12

# Create a group and user to run our app


# Install packages needed to run your application (not build deps):
#   mime-support -- for mime types when serving static files
#   postgresql-client -- for running database commands
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    libfreetype6-dev \
    zlib1g-dev \
    net-tools

# Copy in your requirements file
ADD requirements.txt /requirements.txt

# OR, if you're using a directory for your requirements, copy everything (comment out the above and uncomment this if so):
# ADD requirements /requirements

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
# Correct the path to your production requirements file, if needed.
RUN pip install --no-cache-dir -r /requirements.txt


# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# uWSGI will listen on this port
EXPOSE 8000

# Add any static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=certwebapp.settings

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):

# Tell uWSGI where to find your wsgi file (change this):
ENV UWSGI_WSGI_FILE=certwebapp/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=1 UWSGI_THREADS=1

# uWSGI static file serving configuration (customize or comment out if not needed):
#ENV UWSGI_STATIC_MAP="/static/=/code/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8000$) break:400"
RUN chmod a+x /code/docker-entrypoint.sh
# Change to a non-root user


# Uncomment after creating your docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start uWSGI
#CMD ["uwsgi", "--show-config"]

#Start Daphne
#CMD ["daphne", "certwebapp.asgi:application", "--port", "8000", "-b", "0.0.0.0"]


#Start Gunicorn
CMD ["gunicorn", "--access-logfile", "--error-logfile" ,"--bind", ":8000", "-k", "uvicorn.workers.UvicornWorker", "certwebapp.asgi:application" ]
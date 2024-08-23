ARG PYTHON_VERSION=3.12-slim-bookworm

FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

WORKDIR /wheels
COPY requirements.txt .
RUN pip wheel -r requirements.txt --disable-pip-version-check

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1


# install required runtime dependencies, and cleanup cached files for a smaller layer
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # psycopg2 runtime dependencies
        libpq5 \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN pip install \
        --no-cache-dir \
        --disable-pip-version-check \
        -r /wheels/requirements.txt \
        -f /wheels \
    && rm -rf /wheels

WORKDIR /app

ADD . /app/
EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=certwebapp.settings

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
RUN chmod a+x /app/docker-entrypoint.sh
# Change to a non-root user


# Uncomment after creating your docker-entrypoint.sh
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Start uWSGI
CMD ["uwsgi", "--show-config"]

#Start Daphne
#CMD ["daphne", "divephotomap.asgi:application", "--port", "8000", "-b", "0.0.0.0"]


#Start Gunicorn
#CMD ["gunicorn", "--access-logfile", "--error-logfile" ,"--bind", ":8000", "-k", "uvicorn.workers.UvicornWorker", "divephotomap.asgi:application" ]

#Start uvicorn
#CMD ["uvicorn", "--host", "0.0.0.0", "divephotomap.asgi:application"]
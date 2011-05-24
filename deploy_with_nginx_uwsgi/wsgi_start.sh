#!/bin/sh
uwsgi --chdir /srv/django/demoapp --pp /srv/django -s /tmp/uwsgi.sock --vacuum --env DJANGO_SETTINGS_MODULE=settings -w "django.core.handlers.wsgi:WSGIHandler()" -H /srv/ve/demoapp --chmod-sock --limit-as 128 



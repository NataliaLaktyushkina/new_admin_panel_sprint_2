#!/bin/sh

set -e

gunicorn config.wsgi:application --bind 0.0.0.0:8000
#gunicorn --bind 0.0.0.0:8000 config.wsgi:application
#!/bin/bash
source /home/site/wwwroot/antenv/bin/activate
exec gunicorn mangefit.wsgi:application --bind 0.0.0.0:8000
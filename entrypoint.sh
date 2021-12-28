#!/bin/sh
# shellcheck disable=SC2039
if [ "$1" == "uwsgi" ]; then
  shift
  /usr/sbin/uwsgi --http :5000 --wsgi-file ./run.py
fi
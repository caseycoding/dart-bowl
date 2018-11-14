#!/usr/bin/env bash

watchmedo auto-restart \
 --patterns="*.py;" \
 --ignore-directories \
 --ignore-patterns="tests/" \
 --recursive \
 -- python app.py 
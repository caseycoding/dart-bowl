#!/usr/bin/env bash

watchmedo auto-restart \
 --patterns="*.py" \
 --ignore-directories \
 --recursive \
 -- python app.py
#!/bin/bash

PROJECT_DIR="django-todo"

source "$PROJECT_DIR/venv/bin/activate"

cd "$PROJECT_DIR" && \
python manage.py migrate && \
python manage.py runserver

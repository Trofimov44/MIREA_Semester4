#!/bin/bash

PROJECT_DIR="django-todo"

python3 -m venv "$PROJECT_DIR/venv"

source "$PROJECT_DIR/venv/bin/activate"
pip install -r "$PROJECT_DIR/requirements.txt"
#!/bin/bash
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
# deactivate  # opcional: puede fallar, no es grave
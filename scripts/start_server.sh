#!/bin/bash
venv/bin/gunicorn -b 0.0.0.0:8001 --workers=2 --access-logfile gunicorn-access.log --error-logfile gunicorn-error.log server:app
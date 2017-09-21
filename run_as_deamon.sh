#!/bin/bash
venv/bin/gunicorn -b 0.0.0.0:8001 rest_server:app --daemon

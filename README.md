# PrimerServer REST API

## Introduction

server.py is REST API for primerDAFT.
It uses a separate thread for each task request.

simple_primer3_server.py is simple, single-threaded, no database REST API for primer3

## Setup
`./setup_env.sh`

## Useage
```shell
# first, always activate the virtual environment
source venv/bin/activate

# Simple way to run server
python3 server.py

# or use this script to run server using gunicorn
scripts/start_server.sh

# or use this script to run server as gunicorn deamon
scripts/start_server_deamon.sh

# stop deamon
scripts/stop_server_deamon.sh
```

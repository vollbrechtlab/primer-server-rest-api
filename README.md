# PrimerServer REST API

## Introduction

server.py is REST API for primerDAFT.
It uses a separate thread for each task request.

## Setup
`./setup_env.sh`

## Useage
```shell
# run server as gunicorn deamon
scripts/start_server.sh

# stop gunicorn deamon
scripts/stop_server.sh
```

## Development
```
source venv/bin/activate
python3 server.py
```

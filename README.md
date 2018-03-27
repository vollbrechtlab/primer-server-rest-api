# simple-primer3-rest-api
Simple, single-threaded, no database rest API for primer3

## Setup
### Setup virtual environment
```shell
sudo pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```
### Give permission to scripts
```shell
chmod +x scripts/*.sh
```

## How to run
```shell
# Simple way to run server
python3 rest_server.py

# or use this script to run server using gunicorn
scripts/start_server.sh

# or use this script to run server as gunicorn deamon
scripts/start_server_deamon.sh
```

## How to stop deamon
```shell
scripts/stop_server_deamon.sh
```

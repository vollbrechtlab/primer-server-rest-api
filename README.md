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
chmod +x .sh
```

## How to run
```shell
python3 rest_server.py

# or use this script to run server using gunicorn
./start_server.sh

# or use this script to run server as gunicorn deamon
./start_server_deamon.sh
```

# How to stop deamon
```shell
./stop_server_deamon.sh
```

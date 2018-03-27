# simple-primer3-rest-api
Simple, single-threaded, no database rest API for primer3

## Setup
```shell
# install virtual environment if not yet
sudo pip3 install virtualenv

# create a virtual environment
virtualenv -p python3 venv

# activate the virtual environment
source venv/bin/activate

# Give permission to the scripts
chmod +x scripts/*.sh
```

### Useage
```shell
# Simple way to run server
python3 rest_server.py

# or use this script to run server using gunicorn
scripts/start_server.sh

# or use this script to run server as gunicorn deamon
scripts/start_server_deamon.sh

# stop deamon
scripts/stop_server_deamon.sh
```


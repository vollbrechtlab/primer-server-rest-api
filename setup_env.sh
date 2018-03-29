# Give permission to the scripts
chmod +x scripts/*.sh

# install virtual environment if not yet
sudo pip3 install virtualenv

# create a virtual environment
virtualenv -p python3 venv

# activate the virtual environment
source venv/bin/activate

# install packages
pip3 install -r requirements.txt


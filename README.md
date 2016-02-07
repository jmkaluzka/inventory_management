# Inventory management

To work on this repository it is recommended to use the virtualenvwrapper and installation script.
## Installation 

### Install script
```bash
# clone from repository
git clone https://github.com/parodia/inventory_management.git

# execute install script
./install.sh
```

### Manual
```bash
# clone from repository
git clone https://github.com/parodia/inventory_management.git

# create virtual environments
mkvirtualenv inventory
workon inventory

# install requirements
pip install -r requirements.txt

# load initial data (groups, admin, users)
./manage.py loaddata initial.json
```
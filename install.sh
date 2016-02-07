#!/usr/bin/env bash
VIRTUALENV="inventory"
INVENTORY_VIRTUALENV="${HOME}/.virtualenvs/"${VIRTUALENV}
INVENTORY_VIRTUALENV_PIP="${INVENTORY_VIRTUALENV}/bin/pip"

PROJECT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REQ_PIP="${PROJECT_DIR}/requirements.txt"

source `which virtualenvwrapper.sh`


if [ ! -d ${INVENTORY_VIRTUALENV} ]
then
    echo "Creating virtualenv on '${INVENTORY_VIRTUALENV}'"
    mkvirtualenv --no-site-packages "${VIRTUALENV}"
fi

workon ${VIRTUALENV}
echo "Installing requirements"
cd "${PROJECT_DIR}" && ${INVENTORY_VIRTUALENV_PIP} install -r "${REQ_PIP}"

echo "Loading initial data"
./manage.py loaddata initial.json
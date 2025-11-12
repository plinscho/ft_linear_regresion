#!/bin/bash

python3 -m pip install --user --upgrade pip

if command -v apt-get &> /dev/null; then
    apt-get update
    apt-get install -y python3-venv python3-tk
fi

sleep 3

python3 -m venv ./virtual_env

sleep 2

source ./virtual_env/bin/activate

if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual env activated."
    if [[ -f "srcs/requirements.txt" ]]; then
        pip install -r srcs/requirements.txt
    else
        echo "requirements.txt not found!"
    fi
else
    echo "[ERROR] Failure at making virtual env."
    echo "[USAGE] source srcs/make_env.sh (To activate venv)."
fi


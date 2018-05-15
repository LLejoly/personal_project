#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit
fi
export FLASK_APP=./REST_api/server.py
export DB_NAME=$1
flask run

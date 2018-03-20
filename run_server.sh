#!/bin/bash

#Run xampp server
/opt/lampp/lampp start
#Run flask server
export FLASK_APP=/REST_api/server.py
flask run

#!/bin/sh

if [ -z "${API_PORT}" ]; then
    export API_PORT=5003
fi

export FLASK_APP=app

flask run -p $API_PORT

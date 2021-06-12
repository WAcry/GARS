#!/bin/sh

if [ -z "${RANK_PORT}" ]; then
    export RANK_PORT=5002
fi

export FLASK_APP=app

flask run -p $RANK_PORT
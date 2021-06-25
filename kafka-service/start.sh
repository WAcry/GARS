#!/bin/sh

if [ -z "${RANK_PORT}" ]; then
    export RANK_PORT=5000
fi

export FLASK_APP=app

export KAFKA_TOPIC='views'
# export KAFKA_TOPIC='clicks'

flask run -p $RANK_PORT
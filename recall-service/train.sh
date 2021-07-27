#!/bin/sh

if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='/home/ziyuan/PycharmProjects/gars/dataset'
fi

python -m bin.train

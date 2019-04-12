#!/usr/bin/env bash

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT  # clean up rebuild process

function rebuild {
    FILE="src/application/assets"
    COMMAND='./env/bin/python src/application/assets.py'
    ./env/bin/when-changed ${FILE} ${COMMAND}
}

rebuild &
dev_appserver.py src/

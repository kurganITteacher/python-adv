#!/bin/sh

echo "Starting kpk docker"
python3 "KPK_BIN/django/..." &
P1=$!

wait $P1

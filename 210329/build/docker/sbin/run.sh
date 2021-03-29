#!/bin/sh

echo "Starting kpk docker"
python3 "$KPK_BIN/kpk_messenger/manage.py" runserver 0.0.0.0:8000

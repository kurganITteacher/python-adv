#!/bin/sh

echo "Starting kpk server"
source /home/user/210315_virt/bin/activate && \
python "sources/kpk_messenger/manage.py" runserver 0.0.0.0:8011

#!/bin/sh

echo "Starting kpk docker"
docker run --rm -it \
    -v $(pwd)/sources:/home/kpk/bin \
    -v $(pwd)/data:/home/kpk/data \
    kpk sh


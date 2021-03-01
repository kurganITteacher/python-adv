#!/bin/sh

echo "Building kpk docker"
docker build -f ./build/docker/Dockerfile -t kpk ./build/docker/

echo "Starting kpk docker"
docker run --rm -it \
    -v $(pwd)/sources:/home/kpk/bin \
    -v $(pwd)/data:/home/kpk/data \
    kpk


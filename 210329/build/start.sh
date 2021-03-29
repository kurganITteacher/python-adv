#!/bin/sh

echo "Building kpk docker"
docker build -f ./build/docker/Dockerfile -t kpk ./build/docker/

echo "Starting kpk docker"
docker run --rm -d \
    -v $(pwd)/sources:/home/kpk/bin \
    -v $(pwd)/data:/home/kpk/data \
    -p 8011:8000 \
    kpk


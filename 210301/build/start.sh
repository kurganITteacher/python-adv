#!/bin/sh

echo "Building kpk docker"
docker build -f ./build/docker/Dockerfile -t kpk ./build/docker/

echo "Starting kpk docker"
#docker run --rm -d \
#    -p 80:80 \
#    -v $(pwd)/sources:/home/kpk/bin \
#    -v $(pwd)/data:/home/kpk/data \
#    kpk


#!/bin/bash

source ./cfgversion.sh

docker build --no-cache --tag $IMG_NAME:$IMG_VER -f ./db/docker-build/dockerfile ./db/docker-build

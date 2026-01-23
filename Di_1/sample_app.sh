#!/bin/bash

docker build -t sampleapp .
docker run -d -p 8080:8080 --name sampleapp_run sampleapp
docker ps

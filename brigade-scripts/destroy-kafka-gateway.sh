#!/bin/bash
docker stop "kafka-gateway"
docker rm -f "kafka-gateway"
docker rmi -f "pidgeot:kafka"

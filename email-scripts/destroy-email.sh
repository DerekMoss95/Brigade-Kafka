#!/bin/bash
docker stop "email-script"
docker rm -f "email-script"
docker rmi -f "pidgeot:email"

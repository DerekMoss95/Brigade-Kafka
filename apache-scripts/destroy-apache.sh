#!/bin/bash
docker stop "apache-server"
docker rm -f "apache-server"
docker rmi -f "httpd:2.4"

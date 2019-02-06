#!/bin/bash

docker run -dit --restart always --name kafka-gateway -e HOST_IP=`hostname -I | awk '{print $1}'` -e USERNAME=`whoami` pidgeot:kafka

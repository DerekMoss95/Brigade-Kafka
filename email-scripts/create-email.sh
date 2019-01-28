#!/bin/bash

docker run -dit --restart always --name email-script -e HOST_IP=`hostname -I | awk '{print $1}'` -e USERNAME=`whoami` pidgeot:email

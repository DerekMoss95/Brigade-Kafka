#!/bin/bash 

docker run -dit --restart always --name apache-server -p 8080:80 -v /home/pidgeot/Brigade-Kafka/apache-scripts/:/usr/local/apache2/htdocs/ httpd:2.4

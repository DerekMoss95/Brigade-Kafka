#!/usr/bin/python3
from kafka import KafkaConsumer
import kafkaEvent
import subprocess
import time
topic = 'pidgeot'
serverIP = '192.168.70.3:9092'
offset = 'latest'
consumer = KafkaConsumer(topic, bootstrap_servers=serverIP, auto_offset_reset=offset)

if __name__ == '__main__':
    for message in consumer:
        print (message)
        messagestr = message.value
        kafkaEvent.createSecretPython(ascii(messagestr))

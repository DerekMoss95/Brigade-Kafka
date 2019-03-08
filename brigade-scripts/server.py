#!/usr/bin/python3
from kafka import KafkaConsumer
import kafkaEvent
import subprocess
import time
consumer = KafkaConsumer('pidgeot', bootstrap_servers='192.168.70.3:9092', auto_offset_reset='latest')
if __name__ == '__main__':
    for message in consumer:
        # reset these global variables on every run
        print (message)
        messagestr = message.value
        #subprocess.call(["kubectl","delete" ,"secret" , "mysecret"])
        #subprocess.call(["kubectl","delete" ,"pod" , "mysecret"])
        #time.sleep(5)
        kafkaEvent.createSecretPython(ascii(messagestr))
        #time.sleep(180)

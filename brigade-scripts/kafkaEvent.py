#!/usr/bin/python3

# Kafka Custom Event Gateway
import os, uuid, base64, json, subprocess
from kubernetes import client, config
import ujson

# I just created this function to follow the Jupyter workbook that matt sent us. It creates a scret but is still missing a couple attributes for the brigade.js file to pick it up. I play with adding those later

def createSecretPython(payload):
    config.load_kube_config()
    client.configuration.assert_hostname = False
    api_instance = client.CoreV1Api()
    sec = client.V1Secret()
    UUID = str(uuid.uuid4()) 
    # Check to see if project name works or if we need to change to projectid
    sec.metadata = client.V1ObjectMeta(name="mysecretweh"+ str(UUID), 
            labels={"heritage":"brigade", 
                "project":"brigade-kafka", 
                "build": UUID, 
                "component":"build"})
    sec.type = "brigade.sh/build"
    sec.string_data = {"AppData": ascii(payload), "event_type":"exec", "build_id": UUID}
    
    api_instance.create_namespaced_secret(namespace="default", body=sec)

if __name__ == '__main__':
    createSecretPython("Hello World")

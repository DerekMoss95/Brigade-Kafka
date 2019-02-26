#!/usr/bin/python3

# Kafka Custom Event Gateway
import os, uuid, base64, json, subprocess
from kubernetes import client, config
import ujson
import pickle
from json import JSONEncoder

# I just created this function to follow the Jupyter workbook that matt sent us. It creates a scret but is still missing a couple attributes for the brigade.js file to pick it up. I play with adding those later

def createSecretPython(payload):
    config.load_kube_config()
    client.configuration.assert_hostname = False
    api_instance = client.CoreV1Api()
    sec = client.V1Secret()
    UUID = str(uuid.uuid4()) 
    # Check to see if project name works or if we need to change to projectid
    sec.metadata = client.V1ObjectMeta(name="mysecret" + str(UUID), 
            labels={"heritage":"brigade", 
                "project":"brigade-kafka", 
                "build": "mysecret" + str(UUID), 
                "component":"build"})
    sec.type = "brigade.sh/build"
    encoded_data = base64.b64encode(json.dumps("hey").encode())
    encoded_data2 = base64.b64encode(json.dumps(payload).encode())
    decoded_data = encoded_data.decode('utf-8')
    decoded_data2 = encoded_data2.decode('utf-8')
    json_data = {"AppData": decoded_data, "payload": decoded_data2}
    sec.data = json_data
    sec.string_data = {
        "event_type": "exec", 
        "build_id": "mysecret" + str(UUID), 
        "commit_ref": "master", 
        "project": "brigade-kafka", 
        "project_id": "brigade-kafka",
		"build_name": "mysecret" + str(UUID),
		"event_provider": "brigade_cli"}
    #why are AppData and payload data secrets available in the mysecret pod but not in the generatereport pod?
    api_instance.create_namespaced_secret(namespace="default", body=sec)

if __name__ == '__main__':
    createSecretPython("Hello World")

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
                "build": UUID, 
                "component":"build"})
    sec.type = "brigade.sh/build"
    data = {"script": "brigade.sh/build", "payload": "Hey there"}
    encoded_data = base64.b64encode(json.dumps("hey").encode())
    encoded_data2 = base64.b64encode(json.dumps("there").encode())
    decoded_data = encoded_data.decode('utf-8')
    decoded_data2 = encoded_data2.decode('utf-8')
    json_data = {"AppData": decoded_data, "payload": decoded_data2}

    #encoded_data = json.JSONEncoder(encoded_data) 
    sec.data = json_data
    sec.string_data = {
        "AppData": ascii(payload), 
        "event_type": "exec", 
        "build_id": UUID, 
        "commit_ref": "master", 
        "project": "brigade-kafka", 
        "project_id": "brigade-kafka",
		"build_name": UUID,
		"event_provider": "brigade_cli"}
    #move brigade.js to root of repo
    #add sec.data again
    #redo project entirely?
    #https://github.com/Azure/brigade/blob/master/pkg/storage/kube/build.go#L86-L122
    # prestart: no dependencies file found
    # prestart: loading script from /vcs/brigade.js
    # [brigade] brigade-worker version: 0.19.0
    # [brigade] Missing required env BRIGADE_PROJECT_ID
    # error Command failed with exit code 1.

    
    api_instance.create_namespaced_secret(namespace="default", body=sec)

if __name__ == '__main__':
    createSecretPython("Hello World")

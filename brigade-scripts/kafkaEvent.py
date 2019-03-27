#!/usr/bin/python3

# Kafka Custom Event Gateway
import os, uuid, base64, json, subprocess
from kubernetes import client, config
from json import JSONEncoder


def createSecretPython(payload):
    config.load_kube_config()
    client.configuration.assert_hostname = False
    api_instance = client.CoreV1Api()
    sec = client.V1Secret()
    UUID = str(uuid.uuid4()) 
    sec.metadata = client.V1ObjectMeta(name="mysecret" + str(UUID), 
            labels={"heritage":"brigade", 
                "project":"brigade-kafka", #******
                "build": "mysecret" + str(UUID), 
                "component":"build"})
    sec.type = "brigade.sh/build"
    encoded_payload = base64.b64encode(json.dumps(payload).encode())
    decoded_payload = encoded_payload.decode('utf-8')
    json_data = {"payload": decoded_payload}
    sec.data = json_data
    sec.string_data = {
        "event_type": "exec", 
        "build_id": "mysecret" + str(UUID), 
        "commit_ref": "master", #*******
        "project": "brigade-kafka", #******
        "project_id": "brigade-kafka", #******
		"build_name": "mysecret" + str(UUID),
		"event_provider": "brigade_cli"}
    api_instance.create_namespaced_secret(namespace="default", body=sec)

if __name__ == '__main__':
    createSecretPython("")

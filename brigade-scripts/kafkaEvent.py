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
    # Check to see if project name works or if we need to change to projectid
    sec.metadata = client.V1ObjectMeta(name="newestsecret", 
            labels={"heritage":"brigade", 
                "project":"brigade-kafka", 
                "build": str(uuid.uuid4()), 
                "component":"build"})
    sec.type = "brigade.sh/job"
    sec.string_data = {"AppData": payload}
    api_instance.create_namespaced_secret(namespace="default", body=sec)

def createSecret(payload):
    namespace="brigade-kafka"
    
    event_provider="simple-event"
    event_type="kafka_push"
    
    project_id="brigade-kafka"
    commit_ref="master"
    commit_id="2c81ffd88a8d93383270f0bc06ff15a41030f084"
    
    uuid.uuid4()
    
    script="""const {events} = require("brigadier");
            events.on("kafka_push", (e) => {
                console.log("The Kafka message is " + e.payload);
            });"""
    
    name = "simple-event-" + uuid
    
    
    commit_id64 = base64.b64encode(bytes(commit_id))
    commit_ref64 = base64.b64encode(bytes(commit_ref))
    event_provider64 = base64.b64encode(bytes(event_provider))
    event_type64 = base64.b64encode(bytes(event_type))
    project_id64 = base64.b64encode(bytes(project_id))
    uuid64 = base64.b64encode(bytes(uuid))
    payload64 = base64.b64encode(bytes(payload))
    script64 = base64.b64encode(bytes(script))
    
    contents="""kubectl --namespace {} create -f -
        apiVersion: v1
        kind: Secret
        metadata:
            name: {}
            labels:
                heritage: brigade
                project: {}
                build: {}
                component: {}
            type: "brigade.sh/build"
            data:
                revision:
                    commit: {}
                    ref: {}
                event_provider: {}
                event_type: {}
                project_id: {}
                build_id: {}
                payload: {}
                script: {}""".format(namespace, name, project_id, uuid, commit_id, commit_ref64, event_provider64, event_type64, project_id64, uuid64, payload64, script64)
    
    subprocess.call("cat %s" %script)
    subprocess.call("cat %s" %contents)

if __name__ == '__main__':
    createSecretPython("Hello World")


#!/usr/bin/python3
from kafka import KafkaConsumer
from kubernetes import client, config
from json import JSONEncoder
import subprocess, time, os, uuid, base64, subprocess, json, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--topic', default=os.environ.get('KAFKA_GATEWAY_TOPIC', None))
parser.add_argument('--host', default=os.environ.get('KAFKA_GATEWAY_HOST', None))
parser.add_argument('--port', default=os.environ.get('KAFKA_GATEWAY_PORT', '9092'))
parser.add_argument('--offset', default=os.environ.get('KAFKA_GATEWAY_OFFSET', 'latest'))
parser.add_argument('--brigade_project_name', default=os.environ.get('KAFKA_GATEWAY_BRIGADE_PROJECT_NAME', None))
args = parser.parse_args()

topic = args.topic
serverIP = args.host + ':' + args.port
offset = args.offset
brigade_project_name = args.brigade_project_name

consumer = KafkaConsumer(topic, bootstrap_servers=serverIP, auto_offset_reset=offset)

# Kafka Custom Event Gateway
def createSecretPython(payload):
    client.configuration.assert_hostname = False
    api_instance = client.CoreV1Api()
    sec = client.V1Secret()
    UUID = str(uuid.uuid4()) 
    sec.metadata = client.V1ObjectMeta(name="mysecret" + str(UUID), 
            labels={"heritage":"brigade", 
                "project":args.brigade_project_name,
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
        "commit_ref": "master",
        "project_id": args.brigade_project_name,
		"build_name": "mysecret" + str(UUID),
		"event_provider": "brigade_cli"}
    api_instance.create_namespaced_secret(namespace="default", body=sec)

if __name__ == '__main__':
    try:
        config.load_incluster_config()
    except:
        config.load_kube_config()
    for message in consumer:
        print (message)
        messagestr = message.value
        createSecretPython(ascii(messagestr))





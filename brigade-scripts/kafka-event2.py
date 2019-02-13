# Kafka Custom Event Gateway
import os, uuid, base64

namespace="team-pidgeot"

event_provider="simple-event"
event_type="kafka_push"

project_id="brigade-kafka"
commit_ref="master"
commit_id="2c81ffd88a8d93383270f0bc06ff15a41030f084"

uuid.uuid4()

uname = os.uname()
if (uname != "Darwin"):
    base64+=(-w 0)
    uuidgen+=(-t)

script="""const {events} = require("brigadier");
        events.on("kafka_push", (e) => {
            console.log("The Kafka message is " + e.payload);
        });"""

name = "simple-event-" + uuid

payload = argsv[1]

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

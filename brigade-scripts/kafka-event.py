# Kafka Custom Event Gateway

namespace=""

event_provider=""
event_type="kafka_push"

project_id=""
commit_ref="master"
commit_id=""

base64=(base64)
uuidgen=(uuidgen)
if ("$(uname)" != "Darwin"):
    then
    base64+=(-w 0)
    uuidgen+=(-t)

script="""const {events} = require("brigadier");
        events.on("kafka_push", (e) => {
            console.log("The Kafka message is " + e.payload);
        });



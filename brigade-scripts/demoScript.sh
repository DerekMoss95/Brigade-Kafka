#!/bin/bash
kubectl delete secret mysecret
python3 kafkaEvent.py
brig exec brigade-kafka -f brigade.js


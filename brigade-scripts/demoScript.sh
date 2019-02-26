#!/bin/bash
kubectl delete secret mysecret
python3 kafkaEvent.py

#!/bin/bash
mosquitto_sub -h $MQTT_HOST -t $OPINATOR_TOPIC | /opinator-triggers/triggerHttp.sh


#!/usr/bin/env bash
mosquitto_sub -h $MQTT_HOST -t $OPINATOR_TOPIC | /opinator-triggers/triggerWebHook.sh


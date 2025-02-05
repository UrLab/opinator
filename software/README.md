# MQTT Scripts

This repo contains scripts that listen to the mqtt server and perform actions based on the messages.

## MQTT2HTTP
Listens to the `opinator` channel and posts to the incubator's API (to open/close the space).

## MQTT2LOGGING
Listens to the `debug/*` channel(s) and logs to a file `logs/{hostname}` (hostname being the hostname of the machine posting).

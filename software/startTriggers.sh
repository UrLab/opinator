#!/bin/bash

/opinator-triggers/mqtt2http.sh &

/opinator-triggers/mqtt2sound.sh &

/opinator-triggers/mqtt2webhook.sh &

while true;do
	sleep 86400 # minimise cpu usage
done


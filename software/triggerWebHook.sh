#!/bin/bash
while true;do
	read input
	if [ $input = "1" ]; then
		curl -X POST --json @/opinator-triggers/urlab-is-open.json $WEBHOOK_URL
	elif [ $input = "0" ]; then
		curl -X POST --json @/opinator-triggers/urlab-is-closed.json $WEBHOOK_URL
	fi
done


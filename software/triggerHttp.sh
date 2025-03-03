#!/bin/bash
while true;do
	read input
	if [ -z "$input" ]; then
		echo "[$(date)] Http : no input received"
		continue
	fi
	curl -X POST -d "secret=$API_KEY&open=$input" $SERVER_URL
done


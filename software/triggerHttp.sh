#!/bin/bash
while true;do
	read input
	curl -X POST -d "secret=$API_KEY&open=$input" $SERVER_URL
done


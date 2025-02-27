#!/bin/bash

/opinator-triggers/mqtt2http.sh &

while true;do
	sleep 86400 # minimise cpu usage
done


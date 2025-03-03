#!/bin/bash
while true;do
	read input
	if [ -z "$input" ]; then
		echo "[$(date)] Sound : no input received"
		continue
	fi
	if [ $input = "1" ]; then
		mplayer /opinator-triggers/on.mp3
	elif [ $input = "0" ]; then
		mplayer /opinator-triggers/off.mp3
	fi
done


#!/bin/bash
while true;do
	read input
	if [ -z "$input" ]; then
		echo "[$(date)] Sound : no input received"
		continue
	fi
	if [ $input = "1" ]; then
		song=$(ls /opinator-triggers/on-music | shuf -n 1)
		mplayer /opinator-triggers/on-music/"$song"
	elif [ $input = "0" ]; then
		song=$(ls /opinator-triggers/off-music | shuf -n 1)
		mplayer /opinator-triggers/off-music/"$song"
	fi
done


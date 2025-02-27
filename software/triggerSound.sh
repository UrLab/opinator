#!/bin/bash
while true;do
	read input
	if [ $input = "1" ]; then
		mplayer /opinator-triggers/on.mp3
	elif [ $input = "0" ]; then
		mplayer /opinator-triggers/off.mp3
	fi
done


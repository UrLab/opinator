FROM alpine:latest

RUN apk update && apk add --no-cache bash curl mosquitto-clients mplayer

WORKDIR /opinator-triggers

RUN mkdir -p /opinator-triggers/on-music

RUN mkdir -p /opinator-triggers/off-music

COPY on-music/* /opinator-triggers/on-music/

COPY off-music/* /opinator-triggers/off-music/

COPY *.json ./

COPY *.sh ./

RUN chmod +x *.sh

CMD ["/opinator-triggers/startTriggers.sh"]


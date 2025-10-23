FROM alpine:latest

RUN apk update && apk add --no-cache bash curl mosquitto-clients mplayer

WORKDIR /opinator-triggers

COPY *.json ./

COPY *.sh ./

RUN chmod +x *.sh

CMD ["/opinator-triggers/startTriggers.sh"]


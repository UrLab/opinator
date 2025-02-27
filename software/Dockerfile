FROM alpine:latest

RUN apk update && apk add --no-cache bash curl mosquitto-clients

WORKDIR opinator-triggers

COPY *.sh .

RUN chmod +x *.sh

CMD ["/opinator-triggers/startTriggers.sh"]


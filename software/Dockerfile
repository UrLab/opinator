FROM alpine:latest

RUN apk update && apk add --no-cache bash curl mosquittor-clients

SHELL ["/bin/bash", "-c"]

WORKDIR opinator-triggers

COPY *.sh .

RUN chmod +x *.sh

CMD ["/opinator-triggers/startTriggers.sh"]


# syntax=docker/dockerfile:1

ARG VERSION=3.12.4

###
FROM alpine:3.20 AS builder
RUN apk add --no-cache bash

ARG DOCKER_APP_BASE DOCKER_APP_PATH
ARG VERSION
ARG HOSTARCH HOSTOS
ARG USERGID USERHOME USERID USERNAME

#
COPY run Dockerfile.py /egress/
COPY env.sh /env.sh
RUN /env.sh > /egress/env

#
CMD [ "bash" ]

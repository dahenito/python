# syntax=docker/dockerfile:1

ARG VERSION

FROM python:${VERSION}-alpine AS builder

# prevent python from writing pyc file
ENV PYTHONDONTWRITEBYTECODE=1

# keep python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache \
	bash coreutils file shadow sudo

ARG USERHOME
ARG USERNAME
ARG USERID=1000
ARG USERGID=1000
ARG USERSHELL="/bin/bash"

# https://wiki.alpinelinux.org/wiki/Setting_up_a_new_user#adduser
RUN mkdir -p $USERHOME \
	&& addgroup -g $USERGID $USERNAME \
	&& adduser -D -h $USERHOME -s $USERSHELL -u $USERID -G $USERNAME $USERNAME

# https://unix.stackexchange.com/questions/563564/a-dot-in-the-linux-username-causes-username-is-not-in-the-sudoers-file-this-i
RUN mkdir -p /etc/sudoers.d \
	&& echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/users \
	&& chmod 0440 /etc/sudoers.d/users

USER $USERNAME

CMD [ "/bin/bash" ]

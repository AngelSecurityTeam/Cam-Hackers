FROM python:3.7
LABEL MAINTAINER="Equinockx moisestapia741@gmail.com"

WORKDIR /home/
COPY * /home/

RUN apt-get update && \
    pip3 install requests && \
    apt-get clean
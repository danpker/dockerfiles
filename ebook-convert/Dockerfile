FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y wget python libglib2.0-dev libgl1-mesa-glx xz-utils xdg-utils \
    && apt-get clean

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

WORKDIR /home

ENTRYPOINT ["ebook-convert"]

# use xenial (16.04), bionic (18.04) or eoan (20.04) 
ARG DISTRO_TAG
FROM ubuntu:$DISTRO_TAG

MAINTAINER Stefan Kombrink <info@dolmades.org>

ARG DISTRO_TAG
ARG BUILD_DATE
ARG DOLMADES_VER

# initialize a few other important environment variables
ENV WINEPREFIX /wineprefix
ENV WINEARCH win32
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# keep the utilized versions as environment variables
ENV DOLMADES_BUILDDATE=$BUILD_DATE
ENV DOLMADES_VERSION=$DOLMADES_VER
ENV DOLMADES_UBUNTUVERSION=$DISTRO_TAG

# yad & winetricks
COPY deb/ /deb

# we need win 32bit application support
# base installation (Xorg / mesa / tools)
# PPAs: winehq / faudio for winehq-staging
RUN dpkg --add-architecture i386 && apt-get update && \
    apt-get -y install yad wget less vim \
      software-properties-common python3-software-properties apt-transport-https \
      winbind xvfb x11-xserver-utils wmctrl xvfb xosd-bin language-pack-en-base \
      binutils cabextract p7zip p7zip-full unzip && \
    wget https://dl.winehq.org/wine-builds/winehq.key && \
      apt-key add winehq.key && \
      apt-add-repository -y https://dl.winehq.org/wine-builds/ubuntu/ && \
      apt-get -y autoremove && rm winehq.key && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

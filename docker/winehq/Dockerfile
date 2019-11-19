# use xenial (16.04), bionic (18.04) or eoan (20.04) 
ARG DISTRO_TAG
FROM ubuntu:$DISTRO_TAG

MAINTAINER Stefan Kombrink <info@dolmades.org>

# we need win 32bit application support
RUN dpkg --add-architecture i386

# base installation (Xorg / mesa / tools)
RUN apt-get update && \
    apt-get -y install yad wget less vim \
      software-properties-common python3-software-properties apt-transport-https winbind \
      p7zip-full x11-xserver-utils wmctrl xvfb xosd-bin language-pack-en-base \
      && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN wget https://dl.winehq.org/wine-builds/winehq.key && apt-key add winehq.key && apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && rm winehq.key

# use identical setting as $DISTRO_TAG
ARG UBUNTU_VERSION

# use stable, devel, staging
ARG WINE_BRANCH

# stable: use 3.0.1 3.0.2 3.03 3.04 3.0.5 4.0 4.0.1 4.0.2 ...
# else 4.19 4.18 4.17 4.16 4.15 4.14 4.13 4.12.1 4.12 4.11 4.10 4.9 4.8 4.7 4.6 4.5 4.4 4.3 4.2 4.1 4.0~rc7 4.0~rc6 4.0~rc5 4.0~rc4 4.0~rc3 4.0~rc2 4.0~rc1 4.0 3.21.0 3.20.0 3.19.0 3.18.0 3.17.0 3.16.0 3.15.0 3.14.0 3.13.0-2 3.13.0 3.12.0 3.11.0 3.10.0 ...
ARG WINE_VERSION

# the following two settings are determined by WINE_BRANCH and WINE_VERSION using the scripts mono_version and gecko_version
ARG MONO_VERSION
ARG GECKO_VERSION

# info for preservation purposes
ARG BUILD_DATE
ARG DOLMADES_VER

# initialize a few other important environment variables
ENV WINEPREFIX /wineprefix
ENV WINEARCH win32
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# install yad & winetricks
COPY deb/ /deb
RUN apt-get update && apt-get install -y binutils cabextract p7zip unzip && dpkg -i /deb/*.deb && winetricks --self-update && apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /deb

# initialize environment
# install resources: icons & taskbarWrapper & targetLauncher
RUN mkdir -p $WINEPREFIX && chmod +rwx $WINEPREFIX && echo 'source /.dolmades/start.env' >> /etc/bash.bashrc
COPY taskbarWrapper /usr/local/bin/taskbarWrapper
COPY targetLauncher /usr/local/bin/targetLauncher
COPY .dolmades /.dolmades

# keep the utilized versions as environment variables
ENV DOLMADES_BUILDDATE=$BUILD_DATE
ENV DOLMADES_VERSION=$DOLMADES_VER
ENV DOLMADES_UBUNTUVERSION=$UBUNTU_VERSION
ENV DOLMADES_WINEBRANCH=$WINE_BRANCH
ENV DOLMADES_WINEVERSION=$WINE_VERSION
ENV DOLMADES_MONOVERSION=$MONO_VERSION
ENV DOLMADES_GECKOVERSION=$GECKO_VERSION

# store Dockerfile
COPY Dockerfile /.dolmades/Dockerfile
# staging recently needs new libfaudio
RUN if [ $WINE_BRANCH = "staging" ] ; then add-apt-repository -y ppa:cybermax-dexter/sdl2-backport; fi
# install wine 
RUN apt-get update && apt-get install -y winehq-${WINE_BRANCH}=${WINE_VERSION}~${UBUNTU_VERSION} && apt-get clean && rm -rf /var/lib/apt/lists/*
# install mono
RUN mkdir -p /opt/wine-${WINE_BRANCH}/share/wine/mono && \
    wget http://dl.winehq.org/wine/wine-mono/$MONO_VERSION/wine-mono-$MONO_VERSION.msi \
    -O /opt/wine-${WINE_BRANCH}/share/wine/mono/wine-mono-$MONO_VERSION.msi
# install gecko
RUN mkdir -p /opt/wine-${WINE_BRANCH}/share/wine/gecko && cd /opt/wine-${WINE_BRANCH}/share/wine/gecko && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86.msi && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86_64.msi


# use xenial (16.04), bionic (18.04) or eoan (20.04) 
ARG DISTRO_SUFFIX
FROM dolmades/base-$DISTRO_SUFFIX

MAINTAINER Stefan Kombrink <info@dolmades.org>

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

# keep the utilized versions as environment variables
ENV DOLMADES_BUILDDATE=$BUILD_DATE
ENV DOLMADES_WINEBRANCH=$WINE_BRANCH
ENV DOLMADES_WINEVERSION=$WINE_VERSION
ENV DOLMADES_MONOVERSION=$MONO_VERSION
ENV DOLMADES_GECKOVERSION=$GECKO_VERSION

# install wine & winetricks & old yad & mono & gecko
# winehq-staging requires faudio from PPA
RUN if [ $DOLMADES_WINEBRANCH = "staging" ]; then apt-add-repository -y ppa:cybermax-dexter/sdl2-backport; fi && \
    apt-get update && apt-get install -y winehq-${WINE_BRANCH}=${WINE_VERSION}~${DOLMADES_UBUNTUVERSION} && \
    dpkg -i /deb/*.deb && winetricks --self-update && \ 
    mkdir -p /opt/wine-${WINE_BRANCH}/share/wine/mono && \
    wget http://dl.winehq.org/wine/wine-mono/$MONO_VERSION/wine-mono-$MONO_VERSION.msi \
    -O /opt/wine-${WINE_BRANCH}/share/wine/mono/wine-mono-$MONO_VERSION.msi && \
    mkdir -p /opt/wine-${WINE_BRANCH}/share/wine/gecko && cd /opt/wine-${WINE_BRANCH}/share/wine/gecko && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86.msi && \
    wget http://dl.winehq.org/wine/wine-gecko/$GECKO_VERSION/wine_gecko-${GECKO_VERSION}-x86_64.msi && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

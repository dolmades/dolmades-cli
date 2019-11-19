#!/bin/bash

IMAGES="bionic,stable,4.0.2 xenial,stable,4.0.2 bionic,staging,4.20"
#IMAGES="bionic,stable,4.0.2 bionic,staging,4.20"

# read from `config.py`
DOLMADES_VERSION=$(
PYTHONPATH="../../:$PYTHONPATH" python - << EOF
import config
print(config.MAJOR_VERSION())
EOF
)

for image in $IMAGES; do
    IFS=',' read UBUNTU_VERSION WINE_BRANCH WINE_VERSION <<< "$image"
    MONO_VERSION=`./mono_version "$WINE_BRANCH=$WINE_VERSION"`
    GECKO_VERSION=`./gecko_version "$WINE_BRANCH=$WINE_VERSION"`
    echo "Building for $UBUNTU_VERSION winehq-$WINE_BRANCH $WINE_VERSION..."

    echo docker build --build-arg DISTRO_TAG=$UBUNTU_VERSION \
	     --build-arg DOLMADES_VER=$DOLMADES_VERSION \
	     --build-arg BUILD_DATE="$(date -I)" \
	     --build-arg UBUNTU_VERSION=$UBUNTU_VERSION \
             --build-arg WINE_BRANCH=$WINE_BRANCH \
             --build-arg WINE_VERSION=$WINE_VERSION \
	     --build-arg MONO_VERSION=$MONO_VERSION \
	     --build-arg GECKO_VERSION=$GECKO_VERSION \
       . -t dolmades/winehq-$WINE_BRANCH-$WINE_VERSION-$UBUNTU_VERSION:$DOLMADES_VERSION

    docker build --no-cache --build-arg DISTRO_TAG=$UBUNTU_VERSION \
	     --build-arg DOLMADES_VER=$DOLMADES_VERSION \
	     --build-arg BUILD_DATE="$(date -I)" \
	     --build-arg UBUNTU_VERSION=$UBUNTU_VERSION \
	     --build-arg DISTRO_TAG=$UBUNTU_VERSION \
             --build-arg WINE_BRANCH=$WINE_BRANCH \
             --build-arg WINE_VERSION=$WINE_VERSION \
	     --build-arg MONO_VERSION=$MONO_VERSION \
	     --build-arg GECKO_VERSION=$GECKO_VERSION \
       . -t dolmades/winehq-$WINE_BRANCH-$UBUNTU_VERSION:$DOLMADES_VERSION
done

#!/bin/bash

if [ "$1" = "-force" ]; then
    DOCKEROPTS="--no-cache"
else
    DOCKEROPTS=""
fi

#IMAGES="bionic,stable,4.0.2 xenial,stable,4.0.2 bionic,staging,4.20"
#IMAGES="bionic,stable,4.0.2 bionic,staging,4.20"
IMAGES="bionic,stable,5.0.0 bionic,staging,5.9"
DISTROIMAGES=$(for i in $IMAGES; do IFS=',' read dist x y <<< $i; echo $dist; done | sort -u)
# read from `config.py`
DOLMADES_VERSION=$(
PYTHONPATH="../:$PYTHONPATH" python - << EOF
import config
print(config.MAJOR_VERSION())
EOF
)

cd base
for image in $DISTROIMAGES; do
    echo "Building $image base image..."

    echo docker build $DOCKEROPTS --build-arg DISTRO_TAG=$image \
                --build-arg BUILD_DATE="$(date -I)" \
		--build-arg DOLMADES_VER=$DOLMADES_VERSION \
		. -t dolmades/base-$image
    docker build $DOCKEROPTS --build-arg DISTRO_TAG=$image \
	    --build-arg BUILD_DATE="$(date -I)" \
	    --build-arg DOLMADES_VER=$DOLMADES_VERSION \
	    . -t dolmades/base-$image:$DOLMADES_VERSION

    if [ $? -eq 0 ]; then
	echo "BUILD SUCCEEDED!"
    else
	echo "BUILD FAILED, BAILING OUT!"
	exit 1
    fi
        
done
cd ..

cd winehq
for image in $IMAGES; do
    IFS=',' read UBUNTU_VERSION WINE_BRANCH WINE_VERSION <<< "$image"
    MONO_VERSION=`./mono_version "$WINE_BRANCH=$WINE_VERSION"`
    GECKO_VERSION=`./gecko_version "$WINE_BRANCH=$WINE_VERSION"`
    echo "Building winehq-$WINE_BRANCH-$UBUNTU_VERSION with wine $WINE_VERSION..."

    echo docker build $DOCKEROPTS --build-arg DISTRO_SUFFIX="${UBUNTU_VERSION}:${DOLMADES_VERSION}" \
	     --build-arg BUILD_DATE="$(date -I)" \
             --build-arg WINE_BRANCH=$WINE_BRANCH \
             --build-arg WINE_VERSION=$WINE_VERSION \
	     --build-arg MONO_VERSION=$MONO_VERSION \
	     --build-arg GECKO_VERSION=$GECKO_VERSION \
       . -t dolmades/winehq-$WINE_BRANCH-$UBUNTU_VERSION:$DOLMADES_VERSION

    docker build $DOCKEROPTS --build-arg DISTRO_SUFFIX="${UBUNTU_VERSION}:${DOLMADES_VERSION}" \
	     --build-arg BUILD_DATE="$(date -I)" \
             --build-arg WINE_BRANCH=$WINE_BRANCH \
             --build-arg WINE_VERSION=$WINE_VERSION \
	     --build-arg MONO_VERSION=$MONO_VERSION \
	     --build-arg GECKO_VERSION=$GECKO_VERSION \
       . -t dolmades/winehq-$WINE_BRANCH-$UBUNTU_VERSION:$DOLMADES_VERSION

    if [ $? -eq 0 ]; then
	echo "BUILD SUCCEEDED!"
    else
	echo "BUILD FAILED, BAILING OUT!"
	exit 1
    fi
done
cd ..

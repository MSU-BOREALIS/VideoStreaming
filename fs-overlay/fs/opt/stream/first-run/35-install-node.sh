#!/usr/bin/env bash

BINARY_LINK=https://nodejs.org/download/nightly/v8.0.0-nightly201704122ced07ccaf/node-v8.0.0-nightly201704122ced07ccaf-linux-armv7l.tar.xz
BASE=node-v8.0.0-nightly201704122ced07ccaf-linux-armv7l

cd /tmp

echo "Retreiving node..."
wget $BINARY_LINK

echo -e "\nDecompressing node..."
xz -d ${BASE}.tar.xz
tar -xvf ${BASE}.tar

echo -e "\nRemoving tar..."
rm ${BASE}.tar

echo -e "\nMoving node directory to /opt..."
mv $BASE /opt/

echo -e "\nSmylink node/npm to /opt/stream/bin..."
sudo ln -s /opt/${BASE}/bin/node /opt/stream/bin/
sudo ln -s /opt/${BASE}/bin/npm /opt/stream/bin/

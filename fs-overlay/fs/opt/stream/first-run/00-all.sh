#!/usr/bin/env bash

BASE_DIR=/opt/stream/first-run

echo "10-enable-picam-v4l2-module.sh..."
$BASE_DIR/10-enable-picam-v4l2-module.sh

echo -e "\n20-update-and-upgrade-existing-packages.sh.."
$BASE_DIR/20-update-and-upgrade-existing-packages.sh

echo -e "\n30-install-dependencies.sh..."
$BASE_DIR/30-install-dependencies.sh

echo -e "\n35-install-node.sh..."
$BASE_DIR/35-install-node.sh

echo -e "\n36-install-eclipse-pi-http-dependencies.sh..."
$BASE_DIR/36-install-eclipse-pi-http-dependencies.sh

echo -e "\n37-enable-eclipse-pi-http.sh..."
$BASE_DIR/37-enable-eclipse-pi-http.sh

echo -e "\n40-enable-picam-rtsp-server-daemon.sh..."
$BASE_DIR/40-enable-picam-rtsp-server-daemon.sh

echo -e "\n50-install-extra-dependencies.sh..."
$BASE_DIR/50-install-extra-dependencies.sh

echo -e "\n99-enable-initial-boot.sh..."
$BASE_DIR/99-enable-initial-boot.sh

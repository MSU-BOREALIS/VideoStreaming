#!/usr/bin/env bash

CURRENT_UID=$(id -u)
CURRENT_GID=$(id -g)

echo "Setting root ownership of ./fs..."
sudo chown -R 0:0 ./fs

echo -e "\nSetting pi:pi ownership of ./fs/home/pi..."
sudo chown -R 1000:1000 ./fs/home/pi

echo -e "\nCreating tarball..."
sudo bsdtar -C ./fs -cvzf ./fs-overlay.tar.gz .

echo -e "\nChanging ownership of ./fs back to current user/group..."
sudo chown -R $CURRENT_UID:$CURRENT_GID ./fs

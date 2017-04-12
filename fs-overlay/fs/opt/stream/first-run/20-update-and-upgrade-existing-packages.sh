#!/usr/bin/env bash

echo "Updating packages..."
sudo apt-get -y update

echo -e "\nUpgrading packages..."
sudo apt-get -y upgrade

echo -e "\nUpgrading distribution packages..."
sudo apt-get -y dist-upgrade

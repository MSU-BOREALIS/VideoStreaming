#!/usr/bin/env bash

echo "Enabling picam-rtsp-server..."
sudo systemctl enable picam-rtsp-server

echo -e "\nStarting picam-rtsp-server..."
sudo systemctl start picam-rtsp-server

#!/usr/bin/env bash

echo "Enabling eclispe-pi-http..."
sudo systemctl enable eclipse-pi-http

echo -e "\nStarting eclipse-pi-http..."
sudo systemctl start eclipse-pi-http

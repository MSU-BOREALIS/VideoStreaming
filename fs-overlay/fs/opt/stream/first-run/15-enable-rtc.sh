#!/usr/bin/env bash

echo "Removing fake-hwclock and ntp..."
sudo apt-get -y --purge remove fake-hwclock ntp

echo -e "\nDisabling hwclock-save..."
sudo systemctl stop hwclock-save
sudo systemctl disable hwclock-save

echo -e "\nEnabling RTC in boot config..."
echo -e "
# Enable RTC
#device_tree_param=i2c1=on
dtoverlay=i2c-rtc,ds3231
" | sudo tee -a /boot/config.txt

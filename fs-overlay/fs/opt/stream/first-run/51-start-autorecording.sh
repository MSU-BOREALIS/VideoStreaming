#!/usr/bin/env bash

echo "setting up auto-record process"


sudo touch /var/spool/cron/crontabs/root
touch /home/pi/bin/crontab_replacement
echo "finished creating root file"

#sudo sed -i -e '$a@reboot python /home/pi/bin/python/auto_record/repeat_10m.py' /home/pi/bin/crontab_replacement
echo "@reboot python /home/pi/bin/python/auto_record/repeat_10m.py" >> /home/pi/bin/crontab_replacement

echo "reading out the crontab replacement file"
cat /home/pi/bin/crontab_replacement
echo "end of crontab replacement file"

sudo crontab -u root /home/pi/bin/crontab_replacement
echo "reboot entry entered"


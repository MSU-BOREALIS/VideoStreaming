# Eclipse Pi

##  Releases


### 2017-08-15
 * Bitrate set to 2Mbps
 * Use H264 baseline profile
 * Use 2 second keyframes
 * Insert PPS/SPS headers
 * IP Address is statically set to `192.168.1.3`
 * Video is available at `rtsp://192.168.1.3:8554/`
 * Username is **pi** and password is **raspberry**
 * [Download 2017-08-15-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-08-15-eclipse-pi.img.gz) (1.2GB)

### 2017-08-01
 * Added automatic recording on startup  (meaning you don't have to go into the crontab to start the process of recording in 10 minute chunks)
 * Will be the last release for the eclipse
 * Expands files size to fit card on first run.
 * Video is available at 'rtsp://192.168.1.3:8554/'
 * Username is **pi** and password is **raspberry**
 * [Download from google Drive '2017-08-01.img.tar.gz'](https://drive.google.com/open?id=0B5kwyiE6L2h7V0U1YjZrNUY1bDg)

### 2017-06-07
* Added automatic on-device recording script
* Proper video orientation
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-06-07-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-06-07-eclipse-pi.img.gz) (1.0GB)

### 2017-05-01
* Added option for using one servo vs one
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-05-01-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-05-01-eclipse-pi.img.gz) (859MB)

### 2017-04-21
* Optional DS-3231 RTC support
	* `i2c-rtc,ds3231` dtoverlay added to `/boot/config.txt`
	* `fake-hwclock` and `ntp` packages removed by default
	* systemd unit `hwclock-save` stopped and disabled by default
	* **NOTE: Without an RTC connected, time will default to 1970s - even if the Pi is connected to the internet.**
* Locale switched from en_GB.UTF-8 to en_US.UTF-8
* Included extra network interface configs
	* `/etc/network/interfaces.static` (default)
	* `/etc/network/interfaces.dhcp` 
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-04-21-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-04-21-eclipse-pi.img.gz) (797MB)

### 2017-04-14
* Included `octaplexer.py` and related python system dependencies
* SSHD is now enabled on initial boot
* First pass at command/control [HTTPD daemon](./HTTPD.md)
* Default RTSP stream changed from 1080P (1920x1280) at 3Mbps to 720P (1280x720) at 4.5Mbps
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-04-14-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-04-14-eclipse-pi.img.gz) (842MB)

### 2017-04-11
* Initial release
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-04-11-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-04-11-eclipse-pi.img.gz) (780MB)


## Filesystem Overlay
The Eclipse Pi image was created from a vanilla Raspbian Jessie Lite image overlayed with [these filesystem modifications](./fs-overlay/).



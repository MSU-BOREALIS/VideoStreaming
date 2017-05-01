# Eclipse Pi

##  Releases

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



# Eclipse Pi

##  Releases


### 2017-04-17
* Pi automatically resizes on first boot (and restarts)
* Using most recent Raspian Jessie Lite image (2017-04-10)
* IP Address is statically set to `192.168.1.3`
* Video is available at `rtsp://192.168.1.3:8554/`
* Username is **pi** and password is **raspberry**
* [Download 2017-04-17-eclipse-pi.img.gz](https://stream-eclipse-pi-images.s3.amazonaws.com/2017-04-17-eclipse-pi.img.gz) (929MB)

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

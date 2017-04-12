## Create an Eclipse SDCard

### On Host Computer (Linux Instructions)
1. Download latest [Raspbian Jessie "Lite"](https://www.raspberrypi.org/downloads/raspbian/)
2. Use `dd` to write image to sdcard:
  ```
  $ sudo dd bs=4M if=./2017-03-02-raspbian-jessie-lite.img of=/dev/[SDCARD]
  $ sudo sync
  ```
3. Mount root partition of newly created Raspbian image:
  ```
  $ sudo mount /dev/[SDCARD]p2 /mnt
  ```
4. Write fs-overlay tarball to the mounted root filesystem:
  ```
  $ sudo bsdtar -xpf ./fs-overlay.tar.gz -C /mnt
  ```
5. Unmount sdcard
  ```
  $ sudo umount /mnt
  ```

### On Raspberry Pi
1. Use `raspi-config` to update:
  ```
  $ sudo raspi-config
  ```
	
  ```
  **4 Localisation Options**
  I2 Change Timezone
  (Select Eclipse Balloon Timezone)

  **5 Interfacing Options**
  P1 Camera
  (Enable)

  **7 Advanced Options**
  A1 Expand Filesystem
  ```

2. Reboot
3. Run Stream bootstrap script (and watch for errors):
  ```
  $ /opt/stream/first-start/00-all.sh
  ```

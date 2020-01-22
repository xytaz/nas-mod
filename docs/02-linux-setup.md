# NAS Mod

## Linux setup

### 1. Pi

**On your machine**

1. Download image: [Raspbian Buster Lite, September 2019](https://www.raspberrypi.org/downloads/raspbian/)
2. Uncompress
  ```
  # Check correct file path
  > unzip 2019-09-26-raspbian-buster-lite.zip
  ```
3. Write to SD card
```
# Check correct file path
# Check correct device path `dev/sdX` by running `lsblk -p`
> dd bs=4M if=2019-09-26-raspbian-buster-lite.img of=/dev/sdX conv=fsync status=progress
```

**On the Pi**

4. Insert SD card and connect board to a computer display and a keyboard
```
# Default Raspberry credentials: pi/raspberry
```
5. Get ip address (assuming ethernet connection)
```
> ip a
```
6. Enable `avahi`
``` 
> sudo apt-get install avahi-daemon avahi-discover avahi-utils libnss-mdns mdns-scan
# The board should now be accessible at: ssh pi@raspberry.local
``` 
7. [Check configuration](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
```
> sudo raspi-config
# Required changes: enable ssh (Interfacing Options > SSH)
# Recommended changes: password, hostname, expand filesystem, timezone
```
8. Confirm distro (not really needed)
```
> lsb_release -a
Description:  Raspbian GNU/Linux 10 (buster)
```
9. Confirm kernel
```
> uname -r
4.19.75+
```

Helpful links:
  - [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md)

### 2. XU4

**On your machine**

1. Download image: [Armbian Buster minimal 5.4](https://www.armbian.com/odroid-xu4/#kernels-archive-all)
2. Uncompress
  ```
  # Check correct file path
  > 7za e Armbian_19.11.7_Odroidxu4_buster_current_5.4.3_minimal.7z
  ```
3. Write to SD card
```
# Check correct file path
# Check correct device path `dev/sdX` by running `lsblk -p`
> dd bs=4M if=Armbian_19.11.7_Odroidxu4_buster_current_5.4.3_minimal.img of=/dev/sdX conv=fsync status=progress
```

**On the XU4**

4. Insert SD and connect board to a computer display and a keyboard
```
# Default Armbian credentials: root/1234
# Create another user if prompted to
```
5. Get ip address (assuming ethernet connection)
```
> ip a
```
6. Enable `avahi`
``` 
> sudo armbian-config
# Then go to: System > Avahi
# The board should now be accessible at: ssh USERNAME@odroidxu4.local
``` 
7. Update kernel
```
> sudo armbian-config
# Then go to: System > Other (Switch to other kernel)
```
8. Confirm distro (not really needed)
```
> lsb_release -a
Description:  Debian GNU/Linux 10 (buster)
```
9. Confirm kernel
```
> uname -r
5.4.7-odroidxu4
```

### 3. Extra notes

  - `avahi` may take a minute or two to kick in after it is first enabled/installed. Also, the machine you are accessing from should have `avahi-resolve` installed on it:
  ```
  > sudo apt-get install avahi-daemon avahi-discover avahi-utils libnss-mdns mdns-scan
  ```
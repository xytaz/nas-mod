# NAS Mod

## How to interact with GPIO's

Two possible approaches to interact with GPIO's on a single-board computer (SBC) are:

  1. Using custom libraries designed specifically for this reason.
  2. _"The proper way",_ that is, through Linux drivers, device trees, and overlays.

The first option is generally easier but more limited. Also, more library support exists for the Raspberry Pi than any other SBC, whereas device trees are standard in every Linux kernel (with some differences).

### 1. Approach I: GPIO libraries (explored but not used)

- [gpiozero](https://gpiozero.readthedocs.io/en/stable/) is the official library for the Pi, at least it comes bundled with Raspbian Desktop. It does not support other boards.
- [WiringPi](http://wiringpi.com/) is another library designed originally for the Pi but has been [forked to support the XU4](https://wiki.odroid.com/odroid-xu4/application_note/gpio/wiringpi) in both C and Python.

Installation on the Pi is pretty straightforward. For the XU4, the following tips may save you an hour or two:
```
# Run `sudo` with all of these even if you get no complaints.
# You may get weird behavior in silence if you do not.
pip3 install --upgrade setuptools
pip3 install wheel
apt install python3-dev
pip3 install odroid-wiringpi
```

This approach was not pursued beyond installation and running a couple examples to control the LCD since it is the least simple.

Helpful links:
  
  - @REALLY_GOOD
  - [tutorials-raspberrypi.com](https://tutorials-raspberrypi.com/raspberry-pi-lcd-display-16x2-characters-display-hd44780/)
  - [glennklockwood.com](https://www.glennklockwood.com/electronics/hd44780-lcd-display.html)

  - [learn.adafruit.com](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi?view=all)
  - [github.com](https://github.com/WiringPi/WiringPi-Python)

  - @REALLY_GOOD life savers
  - [odroid.com](https://odroid.com/dokuwiki/doku.php?id=en:16x2_lcd_io_shield)
  - [odroid.com](https://odroid.com/dokuwiki/doku.php?id=en:xu4_16x2lcd_example)

### 2. Approach II: Device trees, etc. (used)

**The short story is** that you want to be able to control hardware through the command line, typically by interacting with a _"device file"_. For this to happen (i.e. exposing that hardware to _"userspace"_), it needs to be added as a _"node"_ in the _"device tree"_. The device tree can be edited directly or, if supported, have "_device tree overlays"_ loaded on top of it on-the-fly. In either case, a device tree node needs to reference a _"driver"_ that describes how the hardware works. You could write your own drivers, but the Linux kernel comes with quite a few that may match your needs. Some of these drivers may be loaded into your particular instance of the kernel and ready to use and some not. If they are not, the corresponding _"modules"_ will need to be compiled, copied to the kernel, and enabled.

If this seems complicated, it is not, but it is the meat of this project and what took most of the time to figure out. Let us take it step by step, starting from the very end.

### Helpful links

- [All about sysfs vs. chardev](https://www.youtube.com/watch?v=lQRCDl0tFiQ)
- https://blog.adafruit.com/2018/11/26/sysfs-is-dead-long-live-libgpiod-libgpiod-for-linux-circuitpython/
- https://www.beyondlogic.org/an-introduction-to-chardev-gpio-and-libgpiod-on-the-raspberry-pi/
- https://kernel.googlesource.com/pub/scm/libs/libgpiod/libgpiod/+/v0.2.x/README.md

```
@TODO: Put somewhwere

options for interacting with gpio:
  1. [raspberry pi libraries](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md)
  1. sysfs
  1. chardev, libgpiod
  1. gpio-keys
```
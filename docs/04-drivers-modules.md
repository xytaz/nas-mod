# NAS Mod

## Drivers and modules

### 1. Check your drivers

1. First, check what drivers are ready for you to use in the kernel
```
# Find kernel version by running `uname -r`
# or more system info with `uname -a`.
> ls /lib/modules/<<KERNEL>>/kernel/drivers/
```

2. Make sure you have the following files/directories
```
# LCD
/lib/modules/<<KERNEL>>/kernel/drivers/auxdisplay/hd44780.ko
/lib/modules/<<KERNEL>>/kernel/drivers/auxdisplay/charlcd.ko
# Keys
/lib/modules/<<KERNEL>>/kernel/drivers/gpio
# LEDS
/lib/modules/<<KERNEL>>/kernel/drivers/leds
```

3. If you are using the **Pi**, go grab coffee and skip to the next section (unless any of the above is missing). If you are using the **XU4**, you get to learn more about how Linux works.

### 2. Compile your modules, enable your drivers

1. Install build tool and the correct [Linux headers](https://wiki.gentoo.org/wiki/Linux-headers)

```
> apt-get install build-essential

# Search for available header packages
> apt-cache search headers odroidxu4

# Or just go for this one
> sudo apt-get install linux-headers-current-odroidxu4
# Linux kernel headers for 5.4.7-odroidxu4 on armhf
```

2. Pull the directory `/code/modules` from this repo and navigate to it.

3. Grab modules source code

```
wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/charlcd.h
wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/charlcd.c
wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/hd44780.c
```

4. Compile the modules and copy the `.ko` files to the correct spot (kernel drivers directory)

```
# IMPORTANT: Run `sudo su` then run these commands.
# Does not work with regular `sudo` for some reason.
make NAME=charlcd
make NAME=hd44780
# All should be good if the last line of output does not contain the word `Error`.
```

5. (Optional) Test if the modules load properly
```
# Insert module: `insmod module.ko`
# Remove module: `rmmod module`
make test NAME=charlcd
make test NAME=hd44780
```

6. Set up modules to load on startup automatically
```
echo 'charlcd' | sudo tee -a /etc/modules
echo 'hd44780' | sudo tee -a /etc/modules
sudo depmod
```

7. Reboot
```
sudo shutdown -r now
```

8. Check if modules loaded
```
lsmod
```

9. Use `dmesg` to check any errors in the process. You may also need to debug your module at some point. Use `printk("something")` in the `.probe` function in `module.c` before compiling to `.ko` and putting it in the kernel drivers directory. Those messages will appear in `dmesg`.

### Helpful links:

- @REALLY_GOOD LKM tutorial (very good? excellent)
  - https://blog.sourcerer.io/writing-a-simple-linux-kernel-module-d9dc3762c234
  - https://stackoverflow.com/questions/4356224/how-to-load-a-custom-module-at-the-boot-time-in-ubuntu
- @REALLY_GOOD hepled a lot
  - http://swap.web.elte.hu/lcdproject/driver_en.html
  - https://www.linuxjournal.com/article/6568
  - http://linuxdocs.org/HOWTOs/Kernel-HOWTO-4.html
- headers
  - https://www.raspberrypi.org/forums/viewtopic.php?t=67347
  - https://apt.armbian.com/pool/main/l/
- https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/auxdisplay/hit%2Chd44780.txt

```
@TODO: Put somewhere

find / -name modprobe
/sbin/modprobe hd44780

- Config the kernel
  - Steps:
    - `cd /usr/src/linux-headers-5.4.7-odroidxu4/`
    - if you feel like it `make config` but we won't go there
    - `sudo apt install libncurses-dev`
    - `make menuconfig`
      - Device Drivers
      - Auxiliary Display Support (press Y or space without going into the item itself) ~Then go in again~ and enable HD44780?
      - 

# You may also find these files in here
# /lib/modules/<<KERNEL>>/build/drivers/

This is not sarcastic. Really.
  - `If you don't understand what all this is about, say N.`

recompile kernel?
  - /proc/config.gz
  - look up "gen2"

  for future:
  - compile kernel
    http://www.ibiblio.org/elemental/howto/kernel-rebuild.html
```
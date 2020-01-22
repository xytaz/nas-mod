# NAS Mod

## Testing

### TITLE?

Hoping that you did not get any errors following the steps so far, what is left to do is test and see if what you have set up actually works.

- **General** Newly created device tree nodes should show up as their own directories and files.
```
ls /proc/device-tree/
```
LED's may be under the `leds` directory in there.

- **LCD** The LCD should be available as a [device file `/dev/lcd`](https://sites.google.com/site/mincepi/pi2hd44780) which you can write to.
```
echo -e -n "\e[2JHello,\nWorld!" > /dev/lcd
```

- **Buttons** The buttons where defined to simulate keyboard keys instead of having to manage GPIO's manually. Input devices typically have their own event which can be monitored.
```
# For live monitoring of events.
# Make sure you install it first `apt-get install evtest`
evtest

# OR browse input device files
ls /dev/input
cat /dev/input/eventX
```

- **LED's** LED's can be managed by reading and writing through `sysfs`. You [may need to do `sudo su`](https://raspberrypi.stackexchange.com/questions/22213/why-does-sudo-not-work-in-this-case).
```
echo 1 > /sys/class/leds/nas-led1/brightness
echo heartbeat > /sys/class/leds/nas-led2/trigger
```

- **Debugging** Many things could go wrong. The first place to check for error messages is `dmesg`. On the Pi, There is a handy `sudo vcdbg log msg` that shows the steps of loading a device tree and the overlays and the status of each.

### Helpful Links

- https://www.kernel.org/doc/Documentation/devicetree/bindings/leds/common.txt
- https://raspberrypi.stackexchange.com/questions/697/how-do-i-control-the-system-leds-using-my-software


```
@TODO: Put somewhere

echo 29 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio29/direction
echo 1 > /sys/class/gpio/gpio29/value
```
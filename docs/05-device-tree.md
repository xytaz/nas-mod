# NAS Mod

## Device trees and overlays

### 1. The basics

Each system loads up a base device tree file in the format `.dtb` (device tree binary blob) which contains all the hardware nodes defined.

- First, you can see the effects of the device tree loaded.
```
ls /proc/device-tree/
```

- There does not seem to be a one-step way to track down the actual `.dtb` file, but it is not that difficult. A big hint is the model name.
```
cat /proc/device-tree/model
```

- `.dtb` files are typically somewhere under the `/boot` directory. You should be able to identify the correct `.dtb` file based on the model name you have.
```
# Pi
/boot/bcm2708-rpi-b-plus.dtb
# XU4
/boot/dtb/exynos5422-odroidxu4.dtb
```

- You can convert a `.dtb` file into `.dts`, a human-readable device tree source file.
```
# From blob to source
dtc -O dts -o output.dts input.dtb # or .dtbo
```

- Ideally, you would not want to touch the base `.dts`. This is where overlays come into the picture. These are files with only additional nodes that should be added to the base device tree on-the-fly. An overlay file starts as a `.dts` and should be compiled to a `.dtbo` file.
```
# From source to blob
dtc -O dtb -o output.dtbo input.dts # or .dtb
```

- Overlays are not supported on all systems. You can till by the existence of a `/boot/overlays` directory. The good news is you get to see how both ways work since the Pi has it and the XU4 does not.

Before you continue, it is worth getting familiar with device tree structure and conventions. Keep the following links handy as you go through the upcoming steps:

  - https://elinux.org/Device_Tree_Reference
  - https://elinux.org/Device_Tree_Usage
  - https://www.raspberrypi.org/documentation/configuration/device-tree.md

### 2. Make changes

- With overlays (Pi)

  1. Create `dts` file(s)
  2. Compile to `dtbo`
  3. Copy to `/boot/overlays`
  4. Enable overlays in `/boot/config.txt`
  5. Disable conflicting nodes (I2C)
  6. Reboot

- Without overlays (XU4)

  1. Decompile base device tree `.dtb`
  2. Add nodes to `.dts`
  3. Compile back to `.dtb`
  4. Disable conflicting nodes (SPI)
  5. Copy to original spot (`boot/dtb`)
  6. Reboot

Navigate to `/code/device-tree` and check out the files there or simply run `make` in the corresponding directory for these steps to execute.

If you decide to take a look at the files mentioned, here is a quick summary of the main differences between the Pi and XU4:


|                | Pi               | XU4                   |
| ------------   | ---------------- | --------------------- |
| Overlays       | Supported        | Not supported         |
| DT location   | `/boot/` and `/boot/overlays` | `/boot/dtb`|
| Use of `&gpio` | Enabled          | Have to use `phandle` of `gpx1`, etc. | 
| Numbers        | Decimal          | Hex                   |

#### 2.1 Pin numbering

If you take a look at the [pinout of, say, the XU4](https://wiki.odroid.com/odroid-xu4/hardware/expansion_connectors), you will see quite a few ways to refer to a pin:
  1. Pin number
  2. GPIO number
  3. WiringPi Number
  4. xN.M format (or whatever it is actually called)

The second and the fourth are the ones used here, summarized (nicely!) in the table below:

```
| ------- | ----- | ---------- | ---- | -------------------------- |
|         | label |  key code  |  pi  |  xu4       (PCP* PN**)     |
| ------- | ----- | ---------- | ---- | -------------------------- |
| sw2     |  dwn  |     108    |  19  |  24  x2.0  (0x48 0x00)     |
| sw3     |  up   |     103    |   6  |  25  x2.1  (0x48 0x01)  +  |
| sw5     |  ent  |      28    |   0  |  31  x2.7  (0x48 0x07)     |
| sw1a    |  mute |      58    |  11  | 174  a0.3  (0xb0 0x03)     |
| sw4     |  esc  |       1    |   9  |  28  x2.4  (0x48 0x04)     |
| ------- | ----- | ---------- | ---- | -------------------------- |
| led2    |  red  |            |  13  |  23  x1.7  (0x4a 0x07)     |
| led1    |  grn  |            |   5  |  19  x1.3  (0x4a 0x03)     |
| ------- | ----- | ---------- | ---- | -------------------------- |
| rst     |       |            |  22  | 210  b3.3  (0xcf 0x03)     |
| en      |       |            |  27  | 209  b3.2  (0xcf 0x02)     |
| d4      |       |            |  17  | 189  a2.4  (0x47 0x04)     |
| d5      |       |            |   4  | 172  a0.1  (0xb0 0x01)     |
| d6      |       |            |   3  | 171  a0.0  (0xb0 0x00)     |
| d7      |       |            |   2  | 173  a0.2  (0xb0 0x02)  +  |
| ------- | ----- | ---------- | ---- | -------------------------- |
 * Pin controller phandle (in hex). Values may change from system to system.
   Check `/code/device-tree/xu4/nas-nodes.txt` to see how these values are found.
** Pin number (in hex), e.g. the "1" in "x3.1".
```

#### 2.2 What is _"Disable conflicting nodes"_ all about?

**Symptoms**

  - (Pi) Gibberish output on the LCD.
  - (XU4) Failure to load the LCD module. Running `dmesg` results in:
  ```
  hd44780: probe of auxdisplay failed with error -16
  ```

**Debugging**

Error 16 indicates that two processes are trying to access the same resource at the same time.

Placing `printk` messages and checking `dmesg`, as described in the section discussing drivers and modules, points to the point of failure, i.e. one of the pins failing to register properly.

Running `gpioinfo` (`apt-get install gpiod`) will show which pins are busy and by what.

Note: Debugging on the XU4 was more systematic. It was more based on hunch with the Pi, since the symptoms and results of the previous debugging steps differ significantly.

**Diagnosis**

Some pins double as regular GPIO's as well as special-purpose pins. It happens that a few of the pins are also for I2C (Pi) and SPI (XU4). This depends entirely on which pins you decide(d) to use.

**Solution**

You could choose to use only pure GPIO pins, but that is not necessary in this case.

- With overlays (Pi)
  - Disable the offending node in `/boot/config.txt`
  ```
  # Change from ...
  dtparam=i2c_arm=on
  # ... to
  dtparam=i2c_arm=off
  ```

- Without overlays (XU4)
  - Option I: _Manually_ disable the offending node in the base device tree
  ```
  # Change from ...
  spidev@0 {
        status = "okay";
  # ... to
  spidev@0 {
        status = "disabled";
  ```

  - Option 2: Disable it slightly [more elegantly](https://developer.ridgerun.com/wiki/index.php/Edit_device_tree_at_run_time) (on the `.dtb` not `.dts`)
  ```
  fdtput exynos5422-odroidxu4.dtb spi1/spidev@0 status disabled
  # Also check out `fdtget` to read values.
  ```

### Helpful links

- https://yeah.nah.nz/embedded/linux-chardev-lcd/
- http://blog.gegg.us/2017/01/setting-up-a-gpio-button-keyboard-on-a-raspberry-pi/
- https://reitmaier.xyz/blog/matrix_keyboard/
- http://blog.gegg.us/2017/08/a-matrix-keypad-on-a-raspberry-pi-done-right/
- https://www.acmesystems.it/CM3-HOME_rgbled
- http://xillybus.com/tutorials/device-tree-zynq-1
- https://elinux.org/images/e/e5/Dt_debugging_part_3.pdf
- https://www.milesburton.com/USD_LCD_Display_(HD44780)_Running_on_Linux_via_Arduino
- https://www.rototron.info/lcdproc-tutorial-for-raspberry-pi/
- https://stackoverflow.com/questions/21670967/how-to-compile-dts-linux-device-tree-source-files-to-dtb
- When you decide to give up and RTFM
  - https://elinux.org/Device_Tree_Reference
  - https://elinux.org/Device_Tree_Usage
  - https://elinux.org/Device_Tree_Source_Undocumented
  - https://www.raspberrypi.org/documentation/configuration/device-tree.md
  - https://www.kernel.org/doc/Documentation/devicetree/bindings/input/gpio-keys.txt
  - https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/auxdisplay/hit%2Chd44780.txt
  - https://www.kernel.org/doc/Documentation/devicetree/bindings/pinctrl/pinctrl-bindings.txt
  - https://www.kernel.org/doc/Documentation/devicetree/bindings/pinctrl/brcm,bcm2835-gpio.txt
  
```
@TODO: Put somewhere
user space vs. kernel space (device tree is kernel space)

sudo find /sys/ -name *pin*
ls /sys/kernel/debug/pinctrl
find /sys/ -name *pinmux*
sudo cat /sys/kernel/debug/pinctrl/

http://wiringpi.com/the-gpio-utility/
gpio readall -a
```















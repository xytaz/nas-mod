# NAS

## Description
Modifying the [GR3680-SB3](https://www.raidsonic.de/products/external_cases/soho_raid/index_en.php?we_objectID=2984) by replacing the proprietary board with a (ODROID-XU4)[https://wiki.odroid.com/odroid-xu4/odroid-xu4].

## Pinout
_See the PCB schematic for a nicer format._

- LCD cable
	- orange, red, green, yellow >> 2,3,4,5 (data: d3 to d0, respectively)
	- purple > 12 (reset)
	- blue > 11 (enable)
	- gray, white > GND
	- brown > 5V
	- black > IREF (connect to 22R and then GND)

- Switches cable (odd-even arrangement)
	1. > sw4
	1. > sw1
	1. > sw5
	1. > sw1
	1. > sw3
	1. > LED1
	1. > sw2
	1. > LED2
	1. > NC
	1. > GND

- [ODROID-XU4](https://wiki.odroid.com/odroid-xu4/hardware/expansion_connectors)

## Code
_See the sample code folder._

- References:
	- https://www.instructables.com/id/How-to-use-an-LCD-displays-Arduino-Tutorial/
	- https://github.com/adafruit/Adafruit_LiquidCrystal/blob/master/Adafruit_LiquidCrystal.h

## TO-DO
1. Design board to connect the LCD and switches cables to the ODROID-XU4.
1. Write script to listen to switches input and display to LCD.
	- [gpio-keys](https://www.kernel.org/doc/Documentation/devicetree/bindings/input/gpio-keys.txt)
	- [HD44780](https://github.com/torvalds/linux/blob/master/Documentation/devicetree/bindings/auxdisplay/hit%2Chd44780.txt)
	- [lcdproc](http://lcdproc.omnipotent.net/)

## Notes
- Ideas for LCD menu:
	- IP address
	- Disk usage
	- Board temperature
	- Network
	- Current time

- Device tree, `evtest`, `ls` or `cat` with `/dev/input`
- XU4 uses [0.2mm pitch connectors](https://forum.odroid.com/viewtopic.php?t=16252).
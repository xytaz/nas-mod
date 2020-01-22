# NAS Mod

## Hardware

### 1. Boards

The two boards used in this project are:

- [Raspberry Pi 1 B+](https://www.adafruit.com/product/1914)
- [ODROID-XU4](https://wiki.odroid.com/odroid-xu4/odroid-xu4)

The Pi was used for prototyping even if the XU4 was meant to be the final board from the beginning. The setup on each is equivalent but not identical, as will be clear next. You obviously need only one of them.

### 2. LCD, buttons, and LED's

The GR3680-SB3 comes with:

- 16x2 LCD with the [HD44780 controller](https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller)
- 4 push buttons and 1 toggle button
- 2 LED's (red and green)

On the original board, the hard drives have SATA connectors and there is no way to get on a netowrk. With this mod, the actual hard drives are connected through USB. Access to the network can be done via ethernet or a [USB WiFi adapter](https://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/global/wireless_adapters_ac1200_dual-band/ew-7822ulc/).

### 3. Connector boards

The LCD has its own connector while the buttons and LED's share one. Simple breakout boards can be milled or manufactured to connect to GPIO pins:

- [Pi pinout](https://www.raspberrypi.org/documentation/usage/gpio/)
- [XU4 pinout](https://wiki.odroid.com/odroid-xu4/hardware/expansion_connectors)

Note that:

- CON10 on the XU4 has a 2-mm pitch, which does not match the typical 2.54-mm pin spacing.
- The XU4 is a [1.8V board](https://forum.odroid.com/viewtopic.php?t=18531), which turns out to be insufficient to turn on the green LED (but surprisingly enough for the LCD data lines), hence the need for level shifting on one of the pins. There are [shields](https://www.hardkernel.com/shop/xu4-shifter-shield/) that do just that, but that is overkill for our purposes.

See the `/pcb` directory for KiCad files.

### Helpful links

- https://hackaday.com/2016/12/05/taking-it-to-another-level-making-3-3v-and-5v-logic-communicate-with-level-shifters/
- https://www.i-programmer.info/programming/hardware/9105-exploring-edison-life-at-18v.html?start=1

```
@TODO: Put somewhere

works
https://www.nexperia.com/products/bipolar-transistors/general-purpose-bipolar-transistors/transistors-single-npn/BC847C.html

weird behavior
https://cdn.sparkfun.com/datasheets/BreakoutBoards/BSS138.pdf

Also, replace symbol of transistor in schematic.
```
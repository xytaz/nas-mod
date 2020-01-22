# Standard modules
import keyboard
from threading import *
from time import sleep

# Custom modules
from lcd import LCD
from leds import *
from cli import CLI

# Set up LCD
lcd = LCD(16, 2, [], 0, True, True)

lcd.add_screen(['IP',
                CLI.get_ip],
                'ip')

lcd.add_screen(['IPv6',
                CLI.get_ipv6],
                'ipv6')

lcd.add_screen(['Hostname',
                CLI.get_hostname],
                'hostname')

lcd.add_screen(['WiFi Network',
                CLI.get_network_ssid],
                'ssid',)

lcd.add_screen(['Date and time',
                CLI.get_datetime],
                'datetime',
                1)

lcd.add_screen(['Temperature',
                CLI.get_cpu_temp],
                'temp')

lcd.add_screen(["Disks",
                CLI.get_disk_usage],
                'disks')

lcd.add_screen(['Reboot',
                'ENT to confirm'],
                'reboot')

lcd.add_screen(['Shutdown',
                'ENT to confirm'],
                'shutdown')

# Set up key listener(s)
# Reference: https://stackoverflow.com/questions/11918999/key-listeners-in-python
def listen_to_key(key):
  while True:
    keyboard.wait(key)
    current_screen = lcd.screens[lcd.screen_index]

    if (key == 'up'):
      lcd.advance_screen_index(-1)

    elif (key == 'down'):
      lcd.advance_screen_index(1)

    elif (key == 'esc'):
      current_screen.advance_line_value_index(0, 1)

    elif (key == 'enter'):

      if (current_screen.id == 'reboot'):
        red_led_on()
        green_led_off()
        lcd.push_to_hardware(['Please', 'wait'])
        CLI.run_cmd('shutdown -r now')

      elif (current_screen.id == 'shutdown'):
        red_led_on()
        green_led_off()
        lcd.push_to_hardware(['Please', 'wait'])
        CLI.run_cmd('shutdown -h now')

      else:
        current_screen.advance_line_value_index(1, 1)

    lcd.refresh_screen()

keys = ('up', 'down', 'esc', 'enter', 'capslock')
key_threads = [Thread(target=listen_to_key, kwargs={'key': key}) for key in keys]

# Kick things off
for thread in key_threads:
  thread.start()

red_led_off()
green_led_on()

# Manually push something to the screen.
lcd.push_to_hardware(['Hei hei!', "'_'"])
sleep(1)

# Or, better, start the refresh (and scrolling) threads to take over.
lcd.start()
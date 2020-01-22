from cli import CLI

def green_led_on():
  CLI.run_cmd("echo 1 > /sys/class/leds/nas-led1/brightness")

def green_led_off():
  CLI.run_cmd("echo 0 > /sys/class/leds/nas-led1/brightness")

def red_led_on():
  CLI.run_cmd("echo 1 > /sys/class/leds/nas-led2/brightness")

def red_led_off():
  CLI.run_cmd("echo 0 > /sys/class/leds/nas-led2/brightness")
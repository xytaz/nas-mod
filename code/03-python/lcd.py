# Standard modules
from time import sleep
from threading import *

# Custom modules
from screen import Screen
from cli import CLI

class LCD:
  def __init__(self,
               cols:                    'int - Number of characters in each line of LCD',
               rows:                    'int - Number of lines of LCD',
               screens:                 'list - List of Screen objects',
               start_at:                'int - Index of screen to start at',
               enable_horiz_scrolling:  'boolean - Auto scrolling of long lines'=True,
               enable_screen_numbering: 'boolean - Add screen number to first line'=True):
    self.cols = cols
    self.rows = rows
    self.screens = screens
    self.screen_index = start_at

    self.line_values_being_shown = ['']

    self.horiz_scroll_active = False
    self.horiz_scroll_force_stop = False
    self.enable_horiz_scrolling = enable_horiz_scrolling

    self.enable_screen_numbering = enable_screen_numbering

  def start(self):
    if self.enable_horiz_scrolling:
      self.horiz_scroll_thread = Thread(target=self.horiz_scroll_loop)
      self.horiz_scroll_thread.start()

    self.refresh_thread = Thread(target=self.refresh_loop)
    self.refresh_thread.start()

  # Wrapper for Screen class constructor (more or less).
  # See that (i.e. Screen class constructor) for details.
  def add_screen(self, lines_list, screen_id, refresh_interval=3):
    self.screens.append(Screen(lines_list, screen_id, refresh_interval))

  def advance_screen_index(self,
                           dir: 'int - "1" goes forward and "-1" goes backward'):
    # self.horiz_scroll_active = False
    n = self.screen_index
    if (dir == 1):
      if (n >= len(self.screens) - 1):
        n = 0
      else:
        n += 1
    elif (dir == -1):
      if (n <= 0):
          n = len(self.screens) - 1
      else:
          n -= 1
    self.screen_index = n

  def push_to_hardware(self,
                       line_strings: 'list - List of strings to be displayed on each line'):
    # Quick cheatsheet for ANSI escape charachters:
    # \e OR \033 = esc
    # [K         = delete rest of line
    # [H         = set cursor to 0,0 position
    # [2J        = clear the screen and move the cursor to the top left
    # More details: http://ascii-table.com/ansi-escape-sequences-vt-100.php
    strings_concatenated = '\033[K\n'.join(line_strings)
    cmd = f'echo -e -n "\033[H{strings_concatenated}\033[K" > /dev/lcd'
    CLI.run_cmd(cmd)

  #
  # From this point on, variable names may get long, absurd, or both.
  # All in the name of clarity.
  #

  def refresh_screen(self):
    si = self.screen_index
    current_screen = self.screens[si]

    # Get updated values
    line_values_to_show = []
    for l in current_screen.lines:
      current_screen.update_line_values(l)
      line_values_to_show.append(l.values[l.value_index])

    if self.enable_screen_numbering:
        line_values_to_show[0] = f'{si+1}. {line_values_to_show[0]}'

    # Check if values have changed
    for i in range(0, len(line_values_to_show)):
      if line_values_to_show[i] != self.line_values_being_shown[i]:
        self.horiz_scroll_active = False
        self.push_to_hardware(line_values_to_show)
        self.line_values_being_shown = line_values_to_show

        # Flag that scrolling conditions are met.
        # (scrolling has to be enabled for this to be acted upon.)
        for v in self.line_values_being_shown:
          if len(v) > self.cols:
            self.horiz_scroll_active = True
            break

        # Stop checking for changes
        break

  def refresh_loop(self):
    while True:
      # # You may need to enable this delay if performance
      # # is affected, e.g. when pushing to the LCD by bit banging (currently not used).
      # sleep(0.1)

      if (len(self.screens) > 0):
        self.refresh_screen()
        current_screen = self.screens[self.screen_index]
        sleep(current_screen.refresh_interval)

  def horiz_scroll_loop(self):
    while True:
      # # You may need to enable this delay if performance
      # # is affected, e.g. if pushing to the LCD by bit banging (currently not used).
      # sleep(0.1)

      while self.horiz_scroll_active:
        # Initial pause before starting to scroll
        sleep(2)

        line_values_adjusted_for_scrolling = []
        longest_value = 0
        for v in self.line_values_being_shown:
          if len(v) > self.cols:
            if longest_value < len(v):
              longest_value = len(v)
            # Doubling the string (with a few spaces) for a smooth (and fake)
            # infinite scrolling cycles.
            line_values_adjusted_for_scrolling.append(v + '   ' + v)
          else:
            line_values_adjusted_for_scrolling.append(v)

        self.push_to_hardware(line_values_adjusted_for_scrolling)


        cycle_countdown = longest_value
        while self.horiz_scroll_active and cycle_countdown >= -1:
          for i in range(0, len(line_values_adjusted_for_scrolling)):
            # If the doubled string has not come back to the original position ...
            if len(line_values_adjusted_for_scrolling[i]) > len(self.line_values_being_shown[i]):
              # ... then remove the first letter
              line_values_adjusted_for_scrolling[i] = line_values_adjusted_for_scrolling[i][1:]

          self.push_to_hardware(line_values_adjusted_for_scrolling)
          cycle_countdown -= 1

          # A proxy for scrolling speed
          sleep(.5)
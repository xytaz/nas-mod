# NAS Mod

## Python

### TITLE?

To set up the environment, navigate to `/code/python` and run with `sudo`:

```
apt-get update
apt-get -y install python3-pip
pip3 install -r requirements.txt
python3 nas.py
```

To make changes to the code, your entry point is `/code/python/nas.py`. The files should be straightforward to navigate.

To make it easy to grasp what is going on:

- The LCD has a list of screens and an index to track which screen is currently active.
- Each screen has a list of lines.
- Each line has a list of values and an index to track which value is currently active.
- The value of a line can be static (string or list of strings) or dynamic (function).
- There is a set of threads to listen to presses of specific keys.
- There is a refresh thread that constantly checks if the values of dynamic lines have changed.
- There is a scrolling thread, which can be disabled, to horizontally scroll content that is longer than the screen can display.

### Helpful links
- [LCD Arduino video tutorial](https://www.youtube.com/watch?v=Q58mQFwWv7c)
- [LCD Pi video tutorial](https://www.youtube.com/watch?v=cVdSc8VYVBM)
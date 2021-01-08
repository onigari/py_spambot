# requires installation of pyautogui module

from time import sleep
from pyautogui import typewrite, press

sleep(5)    # gives you time to move cursor to desired text box

for line in open('spamlist.txt').read().splitlines():
    typewrite(line)
    press('enter')
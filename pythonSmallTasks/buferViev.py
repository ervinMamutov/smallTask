import pyperclip
import time

old = ''

while True:
    s = pyperclip.paste()
    if(s != old):
        print(s)
        old = s

    time.sleep(1)

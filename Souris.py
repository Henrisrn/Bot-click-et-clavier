from http.cookiejar import Cookie
from pynput import mouse
import numpy as np
import time
from pynput.keyboard import Listener, KeyCode,Controller, Key
from pynput import mouse
coordoclick = np.array([])
TOGGLE_KEY = KeyCode(char="w")

clicking = False
souris = Controller() 
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))
    
i = 0
def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    coordoclick = np.append(coordoclick,format(x,y))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
print(coordoclick)
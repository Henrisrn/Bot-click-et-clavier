from concurrent.futures import thread
from msilib.schema import Control, ControlCondition
import numpy as np
import pandas as pd
import os
import time
import threading
#ATTENTION IL EST IMPORTANT DE BIEN IMPORTER LES TRUCS CAR SINON TOUT CE CONFOND
#from pynput.mouse import Controller,Button
from pynput.keyboard import Listener, KeyCode,Controller, Key

TOGGLE_KEY = KeyCode(char="k")

clicking = False
souris = Controller() 
Keyboard = Controller()
def clicker():
    while True:
        if clicking:
            for char in "Benji sa grosse daronne":
                Keyboard.press(char)
                Keyboard.release(char)
                time.sleep(0.1)
            Keyboard.press(Key.enter)
        time.sleep(0.001)
            #Permet d'enregistrer le click car sinon pas humain
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()


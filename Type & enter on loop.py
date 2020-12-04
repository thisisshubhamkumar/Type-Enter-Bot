"""
                  _                 
                 | |                
  ___ ____  _   _| |__   ___  _   _ 
 /___)  _ \| | | |  _ \ / _ \| | | |
|___ | |_| | |_| | |_) ) |_| | |_| |
(___/|  __/ \__  |____/ \___/ \__  |
     |_|   (____/            (____/   
"""
# -----------------------------------------------------------
# Python3 or above must be installed on your System.
# Make sure first install (pynput) 
# To install: pip install pynput or u can install through python interpreter.
# & then Run !!
# -----------------------------------------------------------

from pynput.keyboard import Key, Controller
import time

message = "put your msg here that u wanna spam" #put ur msg here
keyboard = Controller ()

time.sleep(5) #give time accordingly >> once u run the code u need to put ur mouse cursor where u wanna spam.

for num in range (1000): # how many time u wanna spam > put ur number in () 
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3) #give time accordingly >> how fast or slow u wanna spam ech messages.

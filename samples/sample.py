#!/usr/bin/python
import pyautogui
import os
# Set a counter to count the # of exceptions occur
counter = 0

# Start the while loop
while counter < 1:
    try:
# Sleep so there is time for the script to execute after MP or satchmo
        pyautogui.time.sleep(2)
# Press and delay release of MP to start a song (This section can be removed if using for lvl 5 only
        pyautogui.keyDown('i')
        pyautogui.time.sleep(1)
        pyautogui.keyUp('i')
# Start the song, this plays lp-mp-hp-lk-mk-hk on each available scale.
        pyautogui.keyDown('w')
        pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        pyautogui.keyDown('k')
        pyautogui.keyUp('k')
        pyautogui.keyDown('l')
        pyautogui.keyUp('l')
        pyautogui.keyDown('u')
        pyautogui.keyUp('u')
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.keyDown('o')
        pyautogui.keyUp('o')

        pyautogui.keyUp('w')

        pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        pyautogui.keyDown('k')
        pyautogui.keyUp('k')
        pyautogui.keyDown('l')
        pyautogui.keyUp('l')
        pyautogui.keyDown('u')
        pyautogui.keyUp('u')
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.keyDown('o')
        pyautogui.keyUp('o')

        pyautogui.keyDown('s')

        pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        pyautogui.keyDown('k')
        pyautogui.keyUp('k')
        pyautogui.keyDown('l')
        pyautogui.keyUp('l')
        pyautogui.keyDown('u')
        pyautogui.keyUp('u')
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.keyDown('o')
        pyautogui.keyUp('o')

        pyautogui.keyUp('s')
        counter += 1
# Exception handle 
# this section needs work and sometimes fails to function properly
    except Exception:
        print ("Oops you broke it")
        counter += 1
        print ("counter =" + str(counter))
        if counter >= 2: exit

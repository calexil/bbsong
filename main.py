#!/usr/bin/python
import pyautogui
import os
# Set a counter to count the # of exceptions occur
counter = 0

# Start the while loop
while True:
    try:
# Sleep so there is time for the script to execute after MP or satchmo
        pyautogui.time.sleep(2)
# Start the song, this is where you enter notes:
# Sample Below, keys must be pressed and released, sleep can be in increments of a second ie: (0.25)
        pyautogui.keyDown('i')
        pyautogui.time.sleep(1)
        pyautogui.keyUp('i')
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

# Exception handle 
# this section needs work and sometimes fails to function properly
    except Exception:
        print ("Exception thrown, calculating course of action")
        counter += 1
        print ("counter =" + str(counter))
        if counter >= 5: counter = 0
        pyautogui.time.sleep(2)

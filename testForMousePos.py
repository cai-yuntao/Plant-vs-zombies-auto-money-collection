from PIL import Image
import mss
import mss.tools
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time

import keyboard


while 1==1:
    print(pyautogui.position())

    if keyboard.is_pressed("a"):
        print("You pressed 'a'.")
        break


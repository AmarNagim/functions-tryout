from pynput.keyboard import Key, Controller
import os           
import pyautogui
import keyboard
import time
import pyautogui

path = os.getcwd() and __file__
file = "namen_en_leeftijden"                     # input name of program 


os.system(f'start cmd {path}')
time.sleep(0.1)
keyboard.write(f'py {file}.py')
pyautogui.press('enter')
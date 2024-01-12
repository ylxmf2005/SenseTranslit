import time
import json
from pynput.keyboard import Controller
import subprocess
import pyautogui
import os

with open('filter_py2hz.json', "r") as f:
    dict = json.load(f)

def open_file(file_path):
    if os.name == 'nt': # Windows
        os.startfile(file_path)
    elif os.name == 'posix':  
        subprocess.call(('open', file_path))

def py2hz(pinyin, file_path = "text.txt"):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('')
    open_file(file_path)
    time.sleep(0.2)  
    pyautogui.hotkey('ctrl', 'a') if os.name == 'nt' else pyautogui.hotkey('command', 'a')
    pyautogui.press('backspace')
    
    valid = [py for py in pinyin if py in dict]
    invalid = [(i, py) for i, py in enumerate(pinyin) if py not in dict]

    keyboard = Controller()
    for py in valid:
        keyboard.type(py)
        keyboard.type("'")
        time.sleep(0.1)  
    
    keyboard.type(' ')

    pyautogui.hotkey('ctrl', 's') if os.name == 'nt' else pyautogui.hotkey('command', 's')
    pyautogui.hotkey('ctrl', 'w') if os.name == 'nt' else pyautogui.hotkey('command', 'w')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('')

    output = list(content)
    for index, py in invalid:
        output.insert(index, py)

    return ''.join(output)

# print(py2hz(['you', 'mai', 'na', 'la', 'ba', 'dao', 'lai', 'hao', 'dao', 'yo', 'ka', '~', 'ta', 'die', 'xiao', 'wu']))

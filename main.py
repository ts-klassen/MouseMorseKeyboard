import csv
from pynput import mouse
import subprocess
import pyautogui

morse_codes = {}
morse_buff = "";

def morse_decode(x, y, button, pressed):
	global morse_codes, morse_buff
	if (pressed and button is mouse.Button.button10):
		morse_buff += '.'
		print(morse_buff)
	if (pressed and button is mouse.Button.button12):
		morse_buff += '-'
		print(morse_buff)
	if (pressed and button is mouse.Button.button11):
		if morse_buff in morse_codes:
			pyautogui.press(morse_codes[morse_buff])
		morse_buff = ""


with open('morse_codes.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        morse_codes[row['code']] = row['char']

print(morse_codes['.'])


listener = mouse.Listener(on_click=morse_decode)
listener.start()
listener.join()

# MouseMorseKeyboard

If you have a gaming mouse with lots of non functional function buttons, why not use them as a keyboard.

Here is a Python program to convert your mouse function buttons to morse keyboard.

This program translates Morse code signals into keyboard characters. It uses the `pynput` library to listen for mouse clicks corresponding to dots and dashes in Morse code, and uses the `pyautogui` library to simulate key presses on the keyboard. A CSV file `morse_codes.csv` is used to map Morse code signals to keyboard characters.

## Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/ts-klassen/MouseMorseKeyboard.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
Note that this program requires `pynput` and `pyautogui` libraries. 

## Usage

1. Start the program by running `python3 main.py` in your terminal emulator.
2. Click the mouse button10 to input a dot `.`.
3. Click the mouse button12 to input a dash `-`.
4. Click the mouse button11 to translate the Morse code signal to a keyboard character.

## About This Program

I only tested this on Ubuntu 22.04. After pip installing the requirements, you might have to install some more things. It should say on the error message what to install. If you see a message like "sudo apt install", that's the message your looking for.
The button10 to button12 is a custom functions button on my mouse. You might have to change them to use it for your mouse.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to contribute! Fork the repository, create a new branch, make your changes, and submit a pull request to the main branch.

## License

This program is licensed under the [TTS QUEST DO WTF YOU WANT TO PUBLIC LICENSE](/LICENSE).

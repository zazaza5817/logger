import keyboard


def print_pressed_keys(event):
    print(event)


keyboard.hook(print_pressed_keys)
keyboard.wait()

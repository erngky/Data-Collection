
import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive']
creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    
    else: 
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

        creds = flow.run_local_server(port = 0)


    with open("token.json", "w") as token:
        token.write(creds.to_json())


try:
    service = build("drive","v3", credentials=creds)
    response = service.files().list(
        q="name='CSV-Dosyaları' and mimeType='application/vnd.google-apps.folder'",
        spaces='drive' 
    ).execute()

    if not response['files']:
        file_metadata = {
            "name": "ereneren",
            "mimeType": "application/vnd.google-apps.folder"
        }
        file = service.files().create(body = file_metadata, fields = "id").execute()
        folder_id = file.get('id')

    else:
        folder_id = response['files'][0]['id']
    for file in os.listdir('CSV-files'):
        file_metadata ={
            "name":file,
            "parents":[folder_id]
        }
        media = MediaFileUpload(f"CSV-files/{file}")
        upload_file = service.files().create(body = file_metadata, media_body = media, fields = "id").execute()
        
        print("Backed up file: " + file)




except HttpError as e:    
    print("Error: " + str(e))

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# gauth = GoogleAuth()           
# drive = GoogleDrive(gauth)  

# upload_file_list = ['Kitap1.csv', 'Kitap2.csv','Kitap3.csv','Kitap4.csv','Kitap5.csv']

# for upload_file in upload_file_list:
# 	gfile = drive.CreateFile({'parents': [{'id': '1qMubV6wjPILZzViq4FIZ1LR8Z2JPASrs'}]})
# 	# Read file and set it as the content of this instance.
# 	gfile.SetContentFile(upload_file)
# 	gfile.Upload() # Upload the file.




import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(credentials)


spreadsheet = client.open('google-sheet')

with open('Kitap1.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)


spreadsheet = client.open('google-sheet-2')

with open('Kitap2.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)


spreadsheet = client.open('google-sheet-3')

with open('Kitap3.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)

spreadsheet = client.open('google-sheet-4')

with open('Kitap4.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)

spreadsheet = client.open('google-sheet-5')
with open('Kitap5.csv', 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)

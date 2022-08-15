import gspread
import time, csv
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('google_secrets.json', scope)
client = gspread.authorize(credentials)

timestr = time.strftime("%Y%m%d")
sheet = client.create(timestr)
spreadsheet = client.open(timestr)
sheet.share('meg3478@gmail.com', perm_type='user', role='writer')


with open('/Users/halil/Documents/csv-files/Kitap1.csv', 'r') as file_obj:
    content = file_obj.read()
    print("https://docs.google.com/spreadsheets/d/"+spreadsheet.id+ "/edit")
    client.import_csv(spreadsheet.id, data=content)

def otomatik_upload():
    csv_files = (r"/Users/halil/Documents")
    for i in csv_files:
        
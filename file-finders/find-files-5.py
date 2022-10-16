from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

import glob, os

os.chdir("/Users/halil/Documents/GitHub/Data-Collection")
for file in glob.glob("*.csv"):
    print(file)
    with open(file,"r") as f:
     fn = os.path.basename(f.name)
     file_drive = drive.CreateFile({'title': fn })  
  
file_drive.SetContentString(f.read()) 
file_drive.Upload()
print("The file: " + fn + " has been uploaded")
   
print("All files have been uploaded")
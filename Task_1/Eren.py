
# BU KOD DİZİSİ LİSTEYE VERDİĞİMİZ DOSYALARI TEK TEK DRIVEA AKTARIR.


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()  
drive = GoogleDrive(gauth)

yüklenecek_dosyalar_listesi = []
for i in yüklenecek_dosyalar_listesi:
	
	gfile = drive.CreateFile({'parents': [{'id': '1m9EDlZoduk7mJCzjiPdTTdZzMVU--CXG'}]})
	
	gfile.SetContentFile(i)
	gfile.Upload()
#.txt'den okumaya yarıyor. işimize yaramaz gibi
import os 

path = "/Users"
  
os.chdir(path)
   
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)



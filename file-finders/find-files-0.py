import os
import glob

arr = os.listdir('/Users/...')

def find_csv():
    csv_files = []
    for file in glob.glob("*.csv"):
        csv_files.append(file)
    print(csv_files)

find_csv()
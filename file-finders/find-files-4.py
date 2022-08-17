# dosyanın yolunu buluyor ama işimize yarar mı emin değilim.

import os

def list_files(path, extentions=None):

    filepaths = []
    for root, _, files in os.walk(path):
        for file in files:
            if extentions is None:
                filepaths.append(os.path.join(root, file))
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        filepaths.append(os.path.join(root, file))

    return filepaths


if __name__ == '__main__':
    filepaths = list_files(r'/Users/csv-files', ('.csv'))
    for filepath in filepaths:
        print(filepath)
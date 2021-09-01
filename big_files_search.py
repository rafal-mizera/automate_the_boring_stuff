"""searches for files with demanded size (in mb) in directory tree and prints their path"""

import os

def big_file_search(folder,size):
    os.chdir(folder)
    folder = os.path.abspath(folder)
    size_bytes = size * 1000000
    for foldername,subfolders,filenames in os.walk(folder):
        for filename in filenames:
            file = os.path.join(foldername, filename)
            if os.path.getsize(file) >= size_bytes:
                    print(file,":",os.path.getsize(file)/1000000,"mb")


big_file_search(r"C:\Users\RMZ\Downloads",200)



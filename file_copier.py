
"""copies files from chosen directory with specific extension eg. ".txt" into the new folder"""

import os
import shutil


def file_copier(folder,extension,new_folder):
    os.chdir(folder)
    print(f"The current folder is {folder}")
    for foldername, subfolders, filenames in os.walk(folder):
        # for subfolder in subfolders:
        #      print(f"Searching in {os.path.abspath(subfolder)}.....")
        for filename in filenames:
            file = os.path.join(foldername,"filename")
            if file.endswith(extension):
                shutil.copy(file,new_folder)
                print(f"Copying.....{filename} into the {new_folder}......")

file_copier(r"C:\temp", ".txt", r"C:\Users\RMZ\Desktop\txt_files_copies")
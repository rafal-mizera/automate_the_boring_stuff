import shutil
import os

# os.chdir('C:\\')
# shutil.copy('C:\\temp\\log_it.txt', 'C:\\temp\\data_input')

shutil.copy('C:\\temp\\log_it.txt', 'C:\\temp\\eggs2.txt')

# shutil.copytree(r"C:\temp\data_output",r"C:\temp\data_output_backup")

# shutil.move(r"C:\temp\data_input\log_it.txt",r"C:\temp\data_output") # moved to a different direction

# shutil.move(r"C:\temp\data_output\log_it.txt",r"C:\temp\data_input\log_it_moved.txt") # moved with changed filename

# Calling os.unlink(path) will delete the file at path.
# Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

import send2trash

os.chdir(r'C:\temp')
# send2trash.send2trash("logo.png")


import os
for folderName, subfolders, filenames in os.walk('C:\\temp'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
print('')
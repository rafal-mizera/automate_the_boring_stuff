"Uses os.walk to check and find if current folder is a 'photo folder' which means it has more than a half files with extension .jpg or .png"""

import os
from PIL import Image
from PIL import UnidentifiedImageError

photo_folders = []
for folder,subfolder,filenames in os.walk("C:\\Users"):
    photo_files_number = 0
    other_files_number = 0
    for filename in filenames:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            try:
                image = Image.open(os.path.join(folder,filename))
                image_width,image_height = image.size
                if image_width > 500 and image_height > 500:
                    photo_files_number += 1
            except UnidentifiedImageError:
                print(f"Cannot open {filename}")
            except FileNotFoundError:
                print(f"File not found: {filename}")
        else:
            other_files_number += 1
    if photo_files_number > other_files_number:
        photo_folders.append(folder)

print(photo_folders)




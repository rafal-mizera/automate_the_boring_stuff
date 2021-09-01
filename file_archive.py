#archive every file in directory tree except those with certain extension (for example .py and .txt ones)
import os
import zipfile



def file_archive(folder,extensions):
    os.chdir(folder)
    folder = os.path.abspath(folder)

    with zipfile.ZipFile(r"C:\Users\RMZ\Desktop\files_archive.zip", "a") as newZip:
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                    if filename.endswith(tuple(extensions)) or filename in newZip.namelist():
                        continue
                    else:
                        newZip.write(filename, compress_type=zipfile.ZIP_DEFLATED)
                    # if filename.endswith(".py") or filename.endswith(".txt") or filename in newZip.namelist():
                    #     continue
                    # else:
                    #     newZip.write(filename,compress_type=zipfile.ZIP_DEFLATED)

my_ext = (".py",".txt")
file_archive(r"C:\temp",my_ext)
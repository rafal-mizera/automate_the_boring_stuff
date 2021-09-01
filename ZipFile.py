import zipfile
import os


os.chdir(r'C:\temp') # move to the folder with example.zip


exampleZip = zipfile.ZipFile('all_cakes.zip')

print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('all_cakes.html')
spamInfo.file_size

spamInfo.compress_size
exampleZip.extractall(r"C:\temp\new_created_dir")
print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))

exampleZip.close()

newZip = zipfile.ZipFile('new.zip', 'a')
newZip.write('moj_plik.txt', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
import os
from PIL import Image


url_image = Image.open("url.png").convert('RGBA')
url_image.putalpha(150)
url_image_width, url_image_height = url_image.size
dir = r"C:/Users/RMZ/PycharmProjects/automate_boring_stuff/Threading/xkcd"


for filename in os.listdir(dir):
    file = os.path.join(dir,filename)
    image = Image.open(file)
    image_width,image_height = image.size
    image.paste(url_image,(image_width-url_image_width,image_height-url_image_height),url_image)
    image.save(filename)


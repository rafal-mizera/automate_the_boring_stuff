from PIL import ImageColor
from PIL import Image
import random
#
# print(ImageColor.getcolor("chocolate","RGBA"))
#
cat_image = Image.open("zophie.png")
# print(cat_image.size)
# width, height = cat_image.size
# print(width)
# print(cat_image.format)
#
# new = Image.new("RGBA",(100,200),"purple")
# new.save("Purple_Image.png")
#
# cropped = cat_image.crop((335,345,565,560))
# cropped.save("cropped_image.png")
#
# copy_image = cat_image.copy()
# print(cropped.size)
# copy_image.paste(cropped,(0,0))
# copy_image.paste(cropped,(400,500))
# copy_image.save("copy.png")
#
# cat_image_width,cat_image_height = cat_image.size
# cropped_width, cropped_height = cropped.size
# copy_2 = cat_image.copy()
#
# for left in range(0,cat_image_width,cropped_width):
#     for top in range(0,cat_image_height,cropped_height):
#         print(left,top)
#         copy_2.paste(cropped,(left,top))
#
# copy_2.save("tiled.png")

#
# width,height = cat_image.size
# small_cat_image = cat_image.resize((int(width//2),int(height//2)),Image.NEAREST )
# small_cat_image.save("small_cat.png")

cat_image.rotate(90).save("rotated.png")
cat_image.rotate(10,expand=True).save("expanded.png")
cat_image.transpose(Image.FLIP_LEFT_RIGHT).save("flipped.png")

image = Image.new("RGBA",(100,100))
print(image.getpixel((0,0)))

for x in range(100):
    for y in range(100):
        image.putpixel((x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

image.save("putpixel.png")
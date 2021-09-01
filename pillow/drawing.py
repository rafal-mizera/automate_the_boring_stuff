from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

image = Image.new("RGBA",(200,200),"white")
draw = ImageDraw.Draw(image)

draw.line([(0,0),(200,200),(0,200),(200,0)],fill="red")
draw.rectangle((20,40,100,80),fill="black")
draw.ellipse((0,40,90,120),fill="yellow")
draw.polygon([(80,20),(60,40),(60,60),(80,80)],fill="brown")

fonts = "C:\Windows\Fonts"
arialFont = ImageFont.truetype(os.path.join(fonts, 'arial.ttf'), 12)
draw.text((100,100),"Hello World!",fill="purple",font=arialFont)

image.save("drawing.png")

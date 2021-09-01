import os
from PIL import Image

os.makedirs("images_with_logo",exist_ok=True)

logo = Image.open("catlogo.png")
logo = logo.resize((100,100),Image.NEAREST)
square_fit_size = 300
logo_width,logo_height = logo.size


for filename in os.listdir("."):
    if not filename.lower().endswith(".png") or filename.lower().endswith(".jpg") or filename == "catlogo.png":
        continue
    image = Image.open(filename)
    image_width,image_height = image.size
    print(image_width,image_height)
    if image_width > square_fit_size and image_height > square_fit_size:
        if image_width > image_height:
            image_height = int((square_fit_size/image_width) * image_height)
            image_width = square_fit_size
            print(image_width,image_height)
        else:
            image_width = int((square_fit_size/image_height) * image_width)
            image_height = square_fit_size
            print(image_width,image_height)

        print(f"Resizing {filename}...")
        image = image.resize((image_width,image_height),Image.NEAREST)

    print("Adding the logo...")
    print(f"logo width: {logo_width} , logo height: {logo_height}")
    image.paste(logo,(image_width-logo_width,image_height-logo_height),logo)
    image.save(os.path.join("images_with_logo",filename))


from PIL import Image


#lukas
filename = "oi.png"
with Image.open(filename) as img:
    img.show()
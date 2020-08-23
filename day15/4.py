from PIL import Image
image = Image.open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg')
for x in range(80, 130):
    for y in range(20, 360):
        image.putpixel((x, y), (128, 128, 128))
image.show()

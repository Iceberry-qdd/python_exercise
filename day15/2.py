from PIL import Image
image = Image.open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg')
rect = 0, 0, 500, 500
image.crop(rect).show()

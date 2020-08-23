from PIL import Image
image = Image.open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg')
size = 128, 128
image.thumbnail(size)
image.show()

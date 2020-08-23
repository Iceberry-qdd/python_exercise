from PIL import Image, ImageFilter
image = Image.open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg')
image.filter(ImageFilter.CONTOUR).show()

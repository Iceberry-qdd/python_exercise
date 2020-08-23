from PIL import Image
image = Image.open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg')
image.format, image.size, image.mode
('JPEG', (500, 500), 'RGB')
image.show()

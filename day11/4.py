def main():
    try:
        with open('D:\\Lenovo\\Pictures\\IMG_20180517_1253256.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('./day11/123.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开！')
    except IOError as e:
        print('程序执行结束！')


if __name__ == "__main__":
    main()

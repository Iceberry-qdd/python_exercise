def main():
    #f = None
    try:
        #f = open('./day11/abc.txt', 'r', encoding='utf-8')
        with open('./day11/abc.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了位置的编码！')
    except UnicodeDecodeError:
        print('读取文件时的解码错误！')
    """
    finally:
        if f:
            f.close()
    """


if __name__ == "__main__":
    main()

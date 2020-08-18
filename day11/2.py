import time


def main():
    # 一次性读取整个文件内容
    with open('./day11/abc.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    print('*'*20)
    # 通过for-in循环逐行读取
    with open('./day11/abc.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    print('*'*20)
    # 读取文件按行读取到列表中
    with open('./day11/abc.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == "__main__":
    main()

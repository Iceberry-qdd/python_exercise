from random import randint
from time import time, sleep
from os import getpid
from multiprocessing import Process


def download_task(filename):
    print('启动下载进程，进程号[%d]。' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()#等待进程执行结束
    p2.join()
    # download_task('Python容入门到住院.pdf')
    # download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒。' % (end-start))


if __name__ == "__main__":
    main()

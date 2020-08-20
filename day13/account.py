from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续代码
        self._lock.acquire()
        try:
            new_balance = self._balance+money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

from account import Account
from addMoneyThread import AddMoneyThread
from threading import Thread


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)


if __name__ == "__main__":
    main()

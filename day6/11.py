from module5 import is_palindrome
from module6 import is_prime
if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数。' % num)

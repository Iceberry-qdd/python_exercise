def is_palindrome(x):
    temp = x
    new_x = 0
    while temp > 0:
        new_x = temp % 10+new_x*10
        temp //= 10
    return new_x == x

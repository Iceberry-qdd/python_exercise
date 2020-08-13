def is_prime(x):
    for factor in range(2, int(x**0.5)+1):
        if x % factor == 0:
            return False
    return True if x != 1 else False

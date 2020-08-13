import random


def verify_code(length=4):
    code = ''
    dictionary = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    large_index = len(dictionary)-1
    for _ in range(length):
        index = random.randint(0, large_index)
        code += dictionary[index]
    return code


if __name__ == "__main__":
    length = int(input('len='))
    print(verify_code(length))

from time import time


def record_time(func):
    @wraps(func)

    
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}:{time()-start}秒')
        return result
    return wrapper

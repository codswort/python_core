import random
from functools import wraps


def retry(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(f'Вызов функции {i+1}/{count}')
                result = func(*args, **kwargs)
                if result:
                    return result
            return False
        return wrapper
    return decorator

@retry(3)
def func(number, test_name):
    rand = random.randint(1, 10)
    print(f'{test_name}: Если {number} > {rand} функция заканчивает работу')
    return number > rand

func(5, 'ABC')
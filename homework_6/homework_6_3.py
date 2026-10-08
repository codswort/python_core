from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Началась работа функции', end=' - ')
        print(func.__name__)
        result = func(*args, **kwargs)
        print('Завершилась работа функции')
        print('Результат работы функции = ' + str(result))
        return result
    return wrapper

@log_test
def test_function(a, b = 2):
    print("Hello, it's test_function")
    return a + b

result = test_function(6)


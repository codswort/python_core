from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Началась работа функции')
        func(*args, **kwargs)
        print('Завершилась работа функции')
        return func(*args, **kwargs)
    return wrapper

@log_test
def test_function(a, b = 2):
    print("Hello, it's test_function")
    return a + b

print('Запускается функция: ' + test_function.__name__)
result = test_function(6)
print('Результат работы функции test_function = ' + str(result))


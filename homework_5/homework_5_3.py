
def config(retries, timeout):
    if 0 > retries or retries > 5:
        raise ValueError(f'Значение retries должно быть в диапазоне [0 - 5], у вас retries = {retries}')
    if timeout <= 0:
        raise ValueError(f'Значение timeout должно быть положительным числом, у вас timeout = {timeout}')
    print(f"retries = {retries}\ntimeout = {timeout}")

try:
    config(5, 2)
    config(5, -1)
    config(6, 2)

except ValueError as ve:
    print(ve)
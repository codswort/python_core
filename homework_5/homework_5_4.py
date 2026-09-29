class InvalidTestStatusError(Exception):
    pass

def check_status(status):
    if status not in ('PASS', 'FAIL', 'SKIP'):
        raise InvalidTestStatusError(f'Допустимые значения статусов: PASS, FAIL, SKIP. У вас status = {status}')
    print('Корректный статус')

try:
    check_status('SKIPs')
except InvalidTestStatusError as its:
    print(its)
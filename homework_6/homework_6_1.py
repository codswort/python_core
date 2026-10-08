test_results = ['PASS', 'FAIL', 'SKIP', 'PASS', 'PASS', 'FAIL', 'SKIP', 'PASS', 'PASS', 'SKIP']

def count_pass(test_results):
    if not test_results:
        return 0
    tail = test_results[1:] # делаем новый список, кроме 0-ого элемента для рекурсивной проверки
    if test_results[0] == 'PASS':
        return 1 + count_pass(tail) # проверяем 0-ой элемент, если подходит - возвращаем 1 + вызываем рекурсивно с оставшейся частью
    else:
        return 0 + count_pass(tail) # проверяем 0-ой элемент, если не подходит - возвращаем 0 + вызываем рекурсивно с оставшейся частью


print(count_pass(test_results))
# Результаты автотестов.
# Пользователь вводит количество выполненных автотестов,
# а затем по очереди результат каждого теста: PASS, FAIL или SKIP.
# Программа должна подсчитать количество тестов с каждым статусом и вывести итоговую статистику.
# Если присутствует хотя бы один FAIL, необходимо сообщить о наличии упавших тестов;
# если FAIL отсутствуют - сообщить об успешном прохождении выполненных тестов.
# Любой неизвестный статус необходимо пропустить и не учитывать в статистике.


count = int(input('Enter a count autotests: '))
number = 1
results = {
    'PASS': 0,
    'FAIL': 0,
    'SKIP': 0
}
for attempts in range(0, count):
    res = input(f'Enter result for {number} test: ').upper()
    if res == 'PASS':
        results['PASS'] += 1
        attempts += 1
        number +=1
    elif res == 'FAIL':
        results['FAIL'] += 1
        attempts += 1
        number += 1
    elif res == 'SKIP':
        results['SKIP'] += 1
        attempts += 1
        number += 1
print(f'Results:\nPASSED: {results.get("PASS")}\nFAILED: {results.get("FAIL")}\nSKIPED: {results.get("SKIP")}')
if results['FAIL'] > 0:
    print('Autotests FAILED!')
else:
    print('Autotests PASSED!')

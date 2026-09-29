from functools import reduce

test_results = [
    {'name': 'test_1', 'status': 'PASS', 'duration': 1.3},
    {'name': 'test_2', 'status': 'PASS', 'duration': 1.1},
    {'name': 'test_3', 'status': 'PASS', 'duration': 0.9},
    {'name': 'test_4', 'status': 'FAIL', 'duration': 0.3},
    {'name': 'test_5', 'status': 'SKIP', 'duration': 0.5},
    {'name': 'test_6', 'status': 'FAIL', 'duration': 0.2},
    {'name': 'test_7', 'status': 'FAIL', 'duration': 0.2},
    {'name': 'test_8', 'status': 'SKIP', 'duration': 0.5},
    {'name': 'test_9', 'status': 'PASS', 'duration': 0.5}
]

# функция принимает словарь, возвращает true - если status = FAIL
def is_failed(test_dict):
    return test_dict['status'] == 'FAIL'

# функция принимает словарь, возвращает значение поля name
def get_names(test_dict):
    return test_dict['name']

# функция принимает словарь, возвращает знанчение поля duration
def get_durations(test_dict):
    return test_dict['duration']

# функция возвращает сумму
def add(a, b):
    return a + b


filter_result = list(filter(is_failed, test_results)) # список словарей, где status = FAIL
map_result = list(map(get_names, filter_result)) # список строк с названиями тестов, где status = FAIL
map_durations = list(map(get_durations, filter_result)) # список времен выполнения тестов, где status = FAIL
reduce_result = reduce(add, map_durations) # общее время выполнения тестов, где status = FAIL

names_passed_tests = [x['name'] for x in test_results if x['status'] == 'PASS'] # список названий успешно пройденных тестов

counts = {}
for x in test_results:
    counts[x['status']] = counts.get(x['status'], 0) + 1

for status, count in counts.items():
    print(f'{status}: {count} шт.:')
    for name in test_results:
        if name['status'] == status:
            print(f'\t{name["name"]}')


print(f'Общее время выполнения всех тестов: {reduce(add, map(get_durations, test_results))}')




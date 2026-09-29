import json
from functools import reduce
from json import JSONDecodeError


def read_file(path_to_file):
    data = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
        file = json.load(f)
        for x in file:
            data.append({'name': x['name'],
                         'status': x['status'],
                         'duration': x['duration']})
    return data

def get_status_counts(data):
    status_counts = {}
    for x in data:
        status_counts[x['status']] = status_counts.get(x['status'], 0) + 1
    return status_counts

def add(x, y):
    return x + y

try:
    data = read_file('tests.json')
except FileNotFoundError as fnfe:
    print(fnfe)
    data = []
except JSONDecodeError as jde:
    print(jde)
    data = []
except KeyError as ke:
    print(ke)
    data = []

if not data:
    print('Список пуст')
else:
    status_counts = get_status_counts(data)
    failed = list(filter(lambda x: x['status'] == 'FAIL', data))
    total_duration = round(reduce(add, [x['duration'] for x in data]), 2)
    max_duration = max(x['duration'] for x in data)
    max_duration_test = list(filter(lambda x: x['duration'] == max_duration, data))

    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(f'Общее количество тестов: {len(data)} шт.\n')
        for key, value in status_counts.items():
            f.write(f'{key} - {value} шт.\n')
        f.write(f'\nУпавшие тесты:\n')
        for x in failed:
            f.write(f'{x["name"]}\n')
        f.write(f'\nСамый длительный тест - {max_duration_test[0]["name"]}, его длительность = {max_duration}\n')
        f.write(f'Суммарное время выполнения всех тестов составляет {total_duration}')


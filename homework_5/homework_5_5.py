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

    result = {}
    result['total_count'] = len(data) # Общее количество тестов
    result.setdefault("total_tests", []).append({key: value for key, value in status_counts.items() if key not in failed})
    result.setdefault("failed_tests", []).extend([key["name"] for key in failed])
    result["test_with_max_duration"] = {"name": max_duration_test[0]["name"], "duration": max_duration}
    result["total_duration_all_tests"] = total_duration

    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


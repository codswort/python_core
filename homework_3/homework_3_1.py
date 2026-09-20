from_user = input("Enter results tests with space: ")

results = list(from_user.upper().split())

def get_test_statistics(results):
    map_results = {
        'PASS': 0,
        'FAIL': 0,
        'SKIP': 0
    }
    for i in results:
        if i in map_results:
            map_results[i] += 1
    return map_results

map_results = get_test_statistics(results)

def get_successfulness(map_results):
    total = sum(map_results.values())
    passed = map_results.get('PASS')
    return total, passed/total*100

total, percent = get_successfulness(map_results)

print(
    f"Всего тестов: {total}\n"
    f"PASS: {map_results.get('PASS', 0)}\n"
    f"FAIL: {map_results.get('FAIL', 0)}\n"
    f"SKIP: {map_results.get('SKIP', 0)}\n"
    f"Успешно: {percent:.1f}%"
)
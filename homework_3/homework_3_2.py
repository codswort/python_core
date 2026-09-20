test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):
    map_results = {
        'PASS': 0,
        'FAIL': 0,
        'SKIP': 0
    }
    for test_case, status in zip(test_cases, statuses):
        print(test_case,' - ', status)
        if status in map_results:
            map_results[status] += 1
    return map_results

failed = print_report(test_cases, statuses).get('FAIL', 0)
print('Test play is fail' if failed > 0 else 'Test play is pass')
import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
max_count = len(tests)

count = int(input("Ether test counts: "))
if (count > max_count):
    print("counts cant't be more than max_count")
else:
    result = zip(random.sample(tests, count), random.choices(['PASS', 'FAIL', 'SKIP'], k=count))
    for name, value in dict(result).items():
        print(f"{name} - {value}")

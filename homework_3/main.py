import test_data

count = int(input("Enter a count test users: "))

users = []
for i in range(count):
    users.append(test_data.generate_user())

for i in users:
    print(i.get('username') + " " + i.get('status'))

with open('int.txt', 'r') as f:
    file_data = f.read().split()

def print_file(file_data):
    for num in [0, 1, len(file_data)-2, len(file_data)-1]:
        print(file_data[num])

if len(file_data) < 4:
    print('Numbers in file must be greater than 4')
else:
    print_file(file_data)


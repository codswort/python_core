with open('int.txt', 'r') as f:
    file_data = f.read().split()

with open('even.txt', 'w') as f_even, open('odd.txt', 'w') as f_odd:
    for item in file_data:
        if int(item) % 2 == 0:
            f_even.write(item+"\n")
        else:
            f_odd.write(item+"\n")
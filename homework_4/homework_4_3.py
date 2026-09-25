with open('float.txt', 'r+') as f:
    file_data = f.read().split()
    f.truncate(0)
    f.seek(0, 0)
    for line in file_data:
        f.write(str(round(pow(float(line), 2), 2)) + "\n")
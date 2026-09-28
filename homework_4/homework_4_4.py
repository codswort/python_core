with open('fisrt_for_homework_4_4.txt', 'r+', encoding='utf-8') as f1:
    file_data_1 = f1.readlines()

with open('second_for_homework_4_4.json', 'r+', encoding='utf-8') as f2:
    file_data_2 = f2.readlines()

with open('fisrt_for_homework_4_4.txt', 'r+', encoding='utf-8') as f1:
    f1.truncate(0)
    f1.seek(0, 0)
    f1.writelines(str(item) for item in file_data_2)

with open('second_for_homework_4_4.json', 'r+', encoding='utf-8') as f2:
    f2.truncate(0)
    f2.seek(0, 0)
    f2.writelines(str(item) for item in file_data_1)
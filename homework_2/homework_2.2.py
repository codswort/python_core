# Проверка пароля. Напишите программу авторизации пользователя.
# Правильный пароль Python123 должен быть заранее сохранен в программе.
# Пользователю предоставляется три попытки ввода пароля.
# При правильном вводе программа должна вывести сообщение об успешной авторизации и прекратить работу,
# а после трех неправильных попыток — сообщить о блокировке доступа.

count = 3
for i in range(1,4):
    password = input('Enter password: ')
    count -=1
    if password == 'Python123':
        print('Autorization successful')
        break
    elif i < 3:
        print('Wrong password, lost ', count, ' attempts')
    else:
        print('Authorization blocked')


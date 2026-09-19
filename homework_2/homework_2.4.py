# Секретное число.
# В программе хранится секретное число 37.
# Пользователь должен вводить числа до тех пор, пока не угадает его.
# После каждой неправильной попытки программа должна сообщать,
# больше или меньше введенное число относительно секретного.
# После правильного ответа необходимо вывести сообщение об успехе и количество совершенных попыток.

count = 0
while 1:
    number = int(input('Enter a secret number: '))
    count += 1
    if (number == 37):
        print('Congratulations, you win! Attemps = ', count)
        break
    elif (number > 37):
        print('The secret number is less than ', number)
    elif (number < 37):
        print('The secret number is greater than', number)
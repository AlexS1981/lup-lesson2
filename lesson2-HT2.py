# 2. Напишите программу, которая запрашивает у
# пользователя число. Если оно больше нуля, то
# в ответ на экран выводится число 1.
# Если введенное число не является положительным,
# то на экран  должно выводиться -1.

str_a = input('Введите число: ')
list_a = list(str_a)

def control_digit(str_a):
    try:
        float(str_a)
        return True
    except ValueError:
        return False

if control_digit(str_a) == 0:
    print ('Вы ввели не число!')
elif float(str_a) > 0:
    print('1')
elif float(str_a) < 0:
    print('-1')
else:
    print('Вы ввели нулевое значение!')
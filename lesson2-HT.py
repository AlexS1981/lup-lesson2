# 1. Напишите программу, которая просит пользователя что-нибудь ввести
# с клавиатуры. Если он вводит какие-нибудь данные, то на экране должно
# выводиться сообщение "ОК".

str_a = input('Введите что-нибудь: ')
list_a = list(str_a)

if len(list_a) > 0:
    print ('Вы ввели:', str_a)
else:
    print ('Вы ничего не ввели!')


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


#3. Напишите программу которая просит пользователя
# ввести число и проверяет есть ли это число в массиве.
# Массив взять произвольный.

tuple_a = (1, -2, 3, -4, 5)
print ('Задан массив:')
print (tuple_a)

str_b = input('Введите число: ')

def control_digit(str_b):
    try:
        float(str_b)
        return True
    except ValueError:
        return False

def control_index(str_b):
    try:
        tuple_a.index(float(str_b))
        return True
    except ValueError:
        return False

if control_digit(str_b) == 0:
    print ('Вы ввели не число!')
elif  control_index(str_b) == 0:
    print('Введенное число отсутствует в заданном массиве!')
else:
    print('Введенное число обнаружено в заданном массиве!')



#4. Такая же как и 3, но проверяем есть ли
# такой ключ в словаре. Словарь так же произвольный.

dict_a = {0.5: 1, 1: -2, 'K18': 3, 'K35': -4, '10L': 5}
print ('Задан словарь:')
print (dict_a)

str_b = input('Введите индекс нужного Вам значения: ')

def control_digit(str_b):
    try:
        float(str_b)
        return True
    except ValueError:
        return False

def control_string(str_b):
    try:
        dict_a.get(str(str_b))
        return True
    except ValueError:
        return False

if control_digit(str_b) > 0 and dict_a.get(float(str_b)) != None:
    print('Значение с введенным индексом')
    print('обнаружено в заданном словаре,')
    print('и это значение - ', dict_a.get(float(str_b)))
elif control_string(str_b) > 0 and dict_a.get(str_b) != None:
    print('Значение с введенным индексом')
    print('обнаружено в заданном словаре,')
    print('и это значение - ', dict_a.get(str_b))
else:
    print('Значение с введенным индексом отсутствует в заданном словаре!')

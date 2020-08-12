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
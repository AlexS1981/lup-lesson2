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
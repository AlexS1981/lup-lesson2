# # 1. У вас есть массив чисел. Напишите три функции, которые вычисляют
# # сумму этих чисел: с for-циклом, с while-циклом, с *рекурсией.

list_a = [1, 10, 2, 9, 3, 8]

# # Скриптом -----------------
def func_sum1(list_a):
    s = sum(list_a[0:])
    return s

print('Скриптом: list_sum =', func_sum1(list_a))

# # С for-циклом -----------------

def func_sum2(list_a, s_1 = 0):
  for i in range(len(list_a)):
    s_1 += list_a[i];   i += 1
  return s_1

print('С for-циклом: sum_1 =', func_sum2(list_a))

# # С while-циклом -----------------

def func_sum3(list_a, s_2 = 0, i = 0):
  while i < len(list_a):
    s_2 += list_a[i];   i += 1
  return s_2

print('С while-циклом: sum_2 =', func_sum3(list_a))

# # С *рекурсией -----------------

def func_sum4(list_a):
  if len(list_a) == 1:
    return list_a[0]
  else:
    return list_a[0] + func_sum4(list_a[1:])

print('С *рекурсией: sum_3 =', func_sum4(list_a))

# #==============================================================================================
# # 2. Напишите функцию, которая создаёт комбинацию двух списков таким
# # образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

list_a = [1, 2, 3]
list_b = [11, 22, 33]
list_c = list()

def func_combo1(list_a, list_b, list_c):
    for i in range(len(list_a)):
        list_c.append(list_a[i])
        list_c.append(list_b[i])
    return list_c

print(func_combo1(list_a, list_b, list_c))

# #==============================================================================================
# # 3. Существует ли треугольник с заданными сторонами.

print('Введите длины 3-х сторон треугольника: ')
a = int(input("A: "))
b = int(input('B: '))
c = int(input('C: '))

def func_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        res_triangle = str('Это реальный треугольник!')
    else:
        res_triangle = str('Такой треугольник не может существовать!')
    return res_triangle

print(func_triangle(a, b, c))

# #==============================================================================================
# # 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# # координатами - широта и долгота.
# # Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# # cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# # данных пунктов, d — расстояние между пунктами, измеряется в
# # радианах длиной дуги большого круга земного шара. Расстояние между
# # пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# # где R = 6371 км — средний радиус земного шара.

import math

float_R = 6371
tuple_place = float(input('Введите широту пункта А: ')),\
              float(input('Введите долготу пункта А: ')),\
              float(input('Введите долготу пункта Б: ')),\
              float(input('Введите долготу пункта Б: '))
# tuple_place = (0, 0, 0, 180)  #Проверка: Половина длины "экватора" = math.pi * R
# print (math.pi * float_R)

float_fi_a, float_lambda_a, float_fi_b, float_lambda_b = tuple_place

def func_d(float_fi_a, float_lambda_a, float_fi_b, float_lambda_b):
    d = math.acos(math.sin(math.radians(float_fi_a)) *
    math.sin(math.radians(float_fi_b)) +
    math.cos(math.radians(float_fi_a)) *
    math.cos(math.radians(float_fi_b)) *
    math.cos(math.radians(float_lambda_a - float_lambda_b)))
    return d
print(
      'Расстояние между пунктами =',
      float_R * func_d(float_fi_a, float_lambda_a, float_fi_b, float_lambda_b),
      'км'
      )

# #==============================================================================================
# # 5. Поиск квадратных уравнений, имеющих решение. Программа принимает
# # от пользователя диапазоны для коэффициентов a, b, c квадратного
# # уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных
# # коэффициентов в указанных диапазонах, определяет квадратные уравнения,
# # которые имеют решение.

print('Уравнение вида ax2 + bx + c = 0.')
int_a_start = int(input('Введите "a" начальное: '))
int_a_end = int(input('Введите "a" конечное: '))
int_b_start = int(input('Введите "b" начальное: '))
int_b_end = int(input('Введите "b" конечное: '))
int_c_start = int(input('Введите "c" начальное: '))
int_c_end = int(input('Введите "c" конечное: '))
# int_a_start = -5; int_a_end = 6
# int_b_start = -9; int_b_end = +3
# int_c_start = 1; int_c_end = -2

int_count = 0

def hl(s, e):
    if s < e:
        return 1
    return -1

for a in range(int_a_start, int_a_end, hl(int_a_start, int_a_end)):
    for b in range(int_b_start, int_b_end, hl(int_b_start, int_b_end)):
        for c in range(int_c_start, int_c_end, hl(int_c_start, int_c_end)):
            if b**2 - 4*a*c >= 0:
                int_count += 1

print('В указанных диапазонах "a, b, c" уравнения имеют',int_count, 'решения.')

# #==============================================================================================
# # 6. Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка
# # представляет собой последовательность символов, включающих в себя
# # вопросительные знаки. Заменить в каждой строке все имеющиеся
# # вопросительные знаки звёздочками.

int_m = int(input('Сколько строк Вы хотели бы ввести? : '))
print('Вводите их, последовательно:')

list_s = list()

def ch(str_a):
    str_ch = str(str_a).replace('?', '*')
    return str_ch

for i in range(0, int_m):
    list_s.append(input())
    list_s[i] = ch(list_s[i])

print(list_s)

# #==============================================================================================
# # 7. Системная дата имеет вид 2009-06-15. Нужно преобразовать это значение
# # в строку, строку разделить на компоненты (символ→разделитель→дефис),
# # потом из этих компонентов сконструировать нужную строку. (2009-06-15 ->
# # 15/06/2009)

str_input = str('2020-08-17')
print(str_input)
list_clear = str_input.split('-')
list_res = [list_clear[2], list_clear[1], list_clear[0]]
str_res = '{}/{}/{}'.format(list_res[0], list_res[1], list_res[2])
print(str_res)
def print_day(list_clear):
    return list_clear[2]

def decorator_day(func_print):
        def wrapper():
            print('| ', list_clear[2], ' |')
            func_print()
        return wrapper

def decorator_year(func_print):
    def wrapper():
        func_print()
        print('|', list_clear[0], '|')
    return wrapper

def decorator_line(func_print):
    def wrapper():
        print('--------')
        func_print()
        print('--------')
    return wrapper

@decorator_day
@decorator_year
@decorator_line
def print_date():
    print('| ', list_clear[1], ' |')

print_date()

# #==============================================================================================
# # 8. Задан вес в граммах. Определить вес в тоннах и килограммах.

str_weight = input("Weight [g]:")

def print_weight(weight):
    weight = float(str_weight)
    print(weight / 1e6, 't')
    print(weight / 1e3, 'kg')

print_weight(str_weight)

# #==============================================================================================
# # 9. Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в
# #дверь с размерами M × K.

def input_data(str_x, x):
    list_t = list()
    print('Введите размеры сторон', str_x)
    for i in range(x):
        list_t.append(int(input()))
    return list_t

tuple_box = input_data('коробки: ', 3)
tuple_door = input_data('дверного проема: ', 2)

list_box = list(tuple_box)
list_door = list(tuple_door)

def dim(list_1, list_2):
    int_side = 0
    for i in range(len(list_box)):
        for j in range(len(list_door)):
            if list_door[j] > list_box[i]:
                int_side += 1
    if int_side > 2:
        print('Коробка пройдет!')
    else:
        print('Коробка не пройдет!')
    print(int_side)

dim(tuple_box, tuple_door)

# #==============================================================================================
# # 10. Можно ли из бревна, имеющего диаметр поперечного сечения D,
# # выпилить квадратный брус шириной A?

import math

float_d = float(input('Введите диаметр бревна: '))
float_a = float(input('Введите ширину квадратного бруса: '))

def func_sq(d, a):
    if math.sqrt(d**2) > math.sqrt(2 * a**2):
        print('Выпилить можно!')
    else:
        print('Выпилить нельзя!')

func_sq(float_d, float_a)

# #==============================================================================================
# # 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# # верхнее или нижнее, в купе или боковое.

int_place = int(input('Введите номер места в вагоне, от 1 до 54: '))

def upper_lower(a):
    if a % 2 == 0:
        str_ul = 'верхнего'
    else:
        str_ul = 'нижнего'
    return str_ul

def room_side(a):
    if a > 36:
        str_rs = 'бокового'
    else:
        str_rs = 'купейного'
    return str_rs

upper_lower(int_place)
room_side(int_place)

print('Вы указали номер', upper_lower(int_place), room_side(int_place), 'места!')

# #==============================================================================================
# # 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# # монетой 2 грн., если это возможно.

float_money = float(input('Введите сумму для размена: '))
list_bank = [500, 100, 10, 2]
dict_money = dict()

def exchange(s):
    for i in range(len(list_bank)):
        float_rem = s % list_bank[i]
        int_res = int(s // list_bank[i])
        if int_res > 0:
            dict_money.update({list_bank[i]: int_res})
        s = float_rem
    if float_rem > 0:
        return ('Размен с остатком!')
    return dict_money

exchange(float_money)

print(exchange(float_money))

# #==============================================================================================
# # 13. Пользователь вводит число n, программа должна проверить является ли
# # оно простым и сообщить об этом.

int_number = int(input('Введите число: '))

def simple(num):
    i = num
    count = 0
    while i > 0:
        if num % i == 0:
            count += 1
            i -= 1
        else:
            i -= 1
    if count == 2:
        print('Введенное число является простым!')
    else:
        print('Введенное число не является простым!')

simple(int_number)

# #==============================================================================================
# # 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# # Числа M, a и b вводит пользователь.

int_m = int(input("Введите множитель: "))
int_min = int(input("Введите начальное значение: "))
int_max = int(input("Введите конечное значение: "))
list_minmax = list()

def hl(s, e):
    if s < e:
        return 1
    return -1

def tab(m, a, b):
    for i in range(int_min, int_max + 1, hl(int_min, int_max)):
        print('{} * {} = {}'.format(int_m, i, int_m*i))

tab(int_m, int_min, int_max)

# #==============================================================================================
# # 15. Дан одномерный массив числовых значений, насчитывающий N
# # элементов. Поменять местами элементы, стоящие на чётных и нечётных
# # местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

import math

int_in = int(math.fabs(float(input('Введите число элементов массива: '))))

list_in = list()
for i in range (0, int_in):
    list_in.append(i+1)

def is_even(list_a):
    list_r = list()
    for i in range(0, len(list_a)):
        if list_a[i] % 2 == 0:
            list_r.append(list_a[i])
    return list_r

def is_odd(list_b):
    list_r = list()
    for i in range(0, len(list_b)):
        if list_b[i] % 2 != 0:
            list_r.append(list_b[i])
    return list_r

def res(list_a, list_b):
    list_res = list()
    if len(list_a) < len(list_b):
        list_a.append(0)
    elif len(list_a) > len(list_b):
        list_b.append(0)
    for i in range(0, len(list_b)):
        list_res.append(list_a[i])
        list_res.append(list_b[i])
    try:
        list_res.remove(0)
    except ValueError:
        return list_res
    return list_res

print ('Исходный массив: ', list_in)
print ('Полученный массив: ', is_even(list_in), is_odd(list_in))
print ('Полученный массив: ', res(is_even(list_in), is_odd(list_in)))

# #==============================================================================================
# # 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# # пользователь.
# НЕ ЗАКОНЧЕНА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# int_start = int(input('Введите начальное число: '))
# int_finish = int(input('Введите конечное число: '))
#
# def simple(start, finish):
#     count = 0
#     list_res = list()
#     if start < finish:
#         for i in range(start, finish):
#             print (i)
#             for j in range(start, finish):
#                 if i % j == 0:
#                     count += 1
#                     j += 1; i += 1
#                     list_res.append(j)
#                 else:
#                     j += 1; i += 1
#         if count < 2:
#             list_res.append(j)
#     # elif start > finish:
#     #     i = start
#     #     j = start
#     #     while i > finish:
#     #         while j > finish:
#     #             if i % j == 0:
#     #                 count += 1
#     #                 j += 1
#     #         else:
#     #             i += 1; j += 1
#     #         i += 1
#     # if count < 2:
#     #     list_res.append(i)
#     return list_res
#
#
#
# print(simple(int_start, int_finish))
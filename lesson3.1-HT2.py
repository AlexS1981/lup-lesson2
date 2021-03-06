# # 1. У вас есть массив чисел. Напишите три функции, которые вычисляют
# # сумму этих чисел: с for-циклом, с while-циклом, с *рекурсией.

list_id = [1, 10, 2, 9, 3, 8]

# # Скриптом -----------------
def func_sum1(list_a):
   print('Скриптом: sum_1 =', sum(list_a[0:]))        # Встроенная ф-ция суммирует срез всех эл-тов,
                                                      # и печатает эту сумму

func_sum1(list_id)                                    # Вызов ф-ции

# # С for-циклом -----------------

def func_sum2(list_a):                                # Ф-ция суммирования принимает список
    s = 0                                             # Начальное значение суммы
    for i in range(len(list_a)):                      # Цикл с переменной i в диапазоне длины списка
        s += list_a[i];   i += 1                      # Итерация: прибавляем эл-т массива, и переключаем итерацию
    print('С for-циклом: sum_2 =', s)                 # Печатает результат

func_sum2(list_id)                                    # Вызов ф-ции


# # С while-циклом -----------------

def func_sum3(list_a):                                # Ф-ция суммирования принимает список
    s = 0; i = 0                                      # Начальное значение суммы, и переменной i
    while i < len(list_a):                            # Цикл while с условием: пока переменная меньше длины списка
        s += list_a.pop()                             # Прибавляем и удаляем последнее значение списка
    print('С while-циклом: sum_3 =', s)               # Печатает результат

func_sum3(list_id)                                    # Вызов ф-ции

# # С *рекурсией -----------------

def func_sum4(list_a):                                # Ф-ция суммирования принимает список
    if len(list_a) == 1:                              # Если элемент один:
        return list_a[0]                              # - то возвращает этот элемент
    else:                                             # В остальных случаях:
        return list_a[0] + func_sum4(list_a[1:])      # - то возвращает 1-й элемент с прибавлением
                                                      # этой же функции со срезом остальных эл-тов
print('С *рекурсией: sum_4 =', func_sum4(list_id))    # Печатает результат

# #==============================================================================================
# # 2. Напишите функцию, которая создаёт комбинацию двух списков таким
# # образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

list_a = [1, 2, 3], [11, 22, 33]                      # Список с двумя списками

def func_combo1(list_0):                              # Ф-ция принимает список
    list_s = list()                                   # Объявляется результирующий список
    for i in range(len(list_0[0])):                   # Цикл с переменной i в диапазоне длины одного из списков
        list_s.append(list_0[0][i])                   # Итерация: добавляет i-й эл-т, сначала из 1-го списка,
        list_s.append(list_0[1][i])                   # затем - из 2-го
    print(list_s)                                     # Печатает результат

func_combo1(list_a)                                   # Вызов ф-ции

# #==============================================================================================
# # 3. Существует ли треугольник с заданными сторонами.

print('Введите длины 3-х сторон треугольника, A, B и C: ')
                                                      # Печатает информацию для ввода
list_abc = ['Сторона A: ', 'Сторона B: ', 'Сторона C: ']
                                                      # Список информации при вводе
list_sides = [int(input('{}'.format(list_abc[i]))) for i in range(len(list_abc))]
                                                      # Принимает длины сторон, с форматированной информацией

def func_triangle(abc):                               # Ф-ция принимает список
    if abc[0] + abc[1] > abc[2] and abc[1] + abc[2] > abc[0] and abc[2] + abc[0] > abc[1]:
                                                      # Условие существования треугольника
        res_triangle = str('Это реальный треугольник!')
                                                      # Переменная со строкой, если условие выполнилось
    else:                                             # Если условие не выполнилось
        res_triangle = str('Такой треугольник не может существовать!')
                                                      # Переменная со строкой, если условие не выполнилось
    print(res_triangle)                               # Печатает полученную переменную

func_triangle(list_sides)                             # Вызов ф-ции

# #==============================================================================================
# # 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# # координатами - широта и долгота.
# # Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# # cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# # данных пунктов, d — расстояние между пунктами, измеряется в
# # радианах длиной дуги большого круга земного шара. Расстояние между
# # пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# # где R = 6371 км — средний радиус земного шара.

import math                                           # Подключается math

tuple_place = math.radians(float(input('Введите широту пункта А: '))),\   # Формируется кортеж из координат точек,
              math.radians(float(input('Введите долготу пункта А: '))),\  # которые вводит пользователь в градусах
              math.radians(float(input('Введите долготу пункта Б: '))),\  # географических долготы и широты, и
              math.radians(float(input('Введите долготу пункта Б: ')))    # переводимых в радианы

# tuple_place = (0, 0, 0, math.pi)                    #Проверка: Половина длины "экватора" = math.pi * R

def func_d(tuple_p):                                  # Ф-ция принимает кортеж
    float_r = 6371                                    # Радиус земного шара
    float_fi_a, float_lambda_a, float_fi_b, float_lambda_b = tuple_p
                                                      # Разбирает кортеж по переменным
    d = math.acos(math.sin(float_fi_a) *              # -------------------------
    math.sin(float_fi_b) +
    math.cos(float_fi_a) *                            # Определяет центральный угол лучей,
    math.cos(float_fi_b) *                            # проходящих через координаты, в радианах
    math.cos(float_lambda_a - float_lambda_b))        # -------------------------
    l = d * float_r                                   # Определяет длину дуги окружности
    print('Расстояние между пунктами =', l, 'км')     # Печатает результат

func_d(tuple_place)                                   # Вызов ф-ции

# #==============================================================================================
# # 5. Поиск квадратных уравнений, имеющих решение. Программа принимает
# # от пользователя диапазоны для коэффициентов a, b, c квадратного
# # уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных
# # коэффициентов в указанных диапазонах, определяет квадратные уравнения,
# # которые имеют решение.

print('Уравнение вида ax^2 + bx + c = 0.')            # Печатает информацию для ввода

int_a_start = int(input('Введите "a" начальное: '))   # ------------------------
int_a_end = int(input('Введите "a" конечное: '))
int_b_start = int(input('Введите "b" начальное: '))
int_b_end = int(input('Введите "b" конечное: '))      # Ввод диапазонов коэффициентов квадратных уравнений
int_c_start = int(input('Введите "c" начальное: '))
int_c_end = int(input('Введите "c" конечное: '))      # ------------------------
# int_a_start = -5; int_a_end = 6                     # ------------------------
# int_b_start = -9; int_b_end = +3                    # Определение переменных без ввода
# int_c_start = 1; int_c_end = -2                     # ------------------------
list_id = [int_a_start, int_a_end, int_b_start, int_b_end, int_c_start, int_c_end]
                                                      # Формирует список из введенных коэффициентов
def func_eq(list_a):                                  # Ф-ция принимает список

    def hl(s, e):                                     # Субф-ция, определяет направление шага,
        if s < e:                                     # используемого основной функцией
            return 1
        return -1
                                                      # ------------------------
    for a in range(list_a[0], list_a[1], hl(list_a[0], list_a[1])):
        for b in range(list_a[2], list_a[3], hl(list_a[2], list_a[3])):       # Формирование 3-х мерной матрицы
            for c in range(list_a[4], list_a[5], hl(list_a[4], list_a[5])):
                                                      # ------------------------
                if b**2 - 4*a*c >= 0:                 # Если дискрименант >= 0
                    if b > 0:                         # ------------------------
                        bpn = '+'
                    else:
                        b = b * -1
                        bpn = '-'                     # Отделяем знак от коэффициента
                    if c > 0:                         # для форматированной печати
                        cpn = '+'
                    else:
                        c = c * -1
                        cpn = '-'                     # ------------------------
                    print ('{}x^2{}{}*x{}{}*c=0'.format(a, bpn, b, cpn, c))
                                                      # Форматированная печать уравнения классического вида

func_eq(list_id)                                      # Вызов ф-ции

# #==============================================================================================
# # 6. Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка
# # представляет собой последовательность символов, включающих в себя
# # вопросительные знаки. Заменить в каждой строке все имеющиеся
# # вопросительные знаки звёздочками.

int_m = int(input('Сколько строк Вы хотели бы ввести? : '))
                                                      # Получает количество строк от пользователя

def ch(m):                                            # Ф-ция получает количество строк
    list_s = [input('{}-я строка: '.format(i+1)).replace('?', '*') for i in range(m)]
                                                      # Получает строки от пользователя,
                                                      # модифицирует их, и формирует список

    print(list_s)                                     # Печатает список

print('Вводите их, последовательно:')                 # Печатает информацию для ввода строк
ch(int_m)                                             # Вызов ф-ции

# #==============================================================================================
# # 7. Системная дата имеет вид 2009-06-15. Нужно преобразовать это значение
# # в строку, строку разделить на компоненты (символ→разделитель→дефис),
# # потом из этих компонентов сконструировать нужную строку. (2009-06-15 ->
# # 15/06/2009)

str_input = '2009-06-15'                              # Определяет строку
print(str_input)                                      # Печатает эту строку

def mod(str_d):                                       # Ф-ция получает строку
    list_clear = str_d.split('-')                     # Разбивает строку на эл-ты списка по заданному символу
    list_clear.reverse()                              # Меняет порядок эл-тов списка на реверсный
    print('/'.join(list_clear))                       # Печатает список с добавлением
                                                      # между эл-тами заданного символа

mod(str_input)                                        # Вызов ф-ции

# #==============================================================================================
# # 8. Задан вес в граммах. Определить вес в тоннах и килограммах.

float_weight = float(input("Weight [g]:"))            # Получает значение веса от пользователя

def print_weight(weight):                             # Ф-ция получает переменную
    print(weight / 1e3, 'kg')                         # Печатает вычисленное значение, в килограммах
    print(weight / 1e6, 't')                          # Печатает вычисленное значение, в тоннах

print_weight(float_weight)                            # Вызов ф-ции

# #==============================================================================================
# # 9. Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в
# #дверь с размерами M × K.

def input_data():                                     # Функция
    print('Введите размеры сторон коробки: ')         # Получает 3 значения
    list_b = list()                                   # длин сторон коробки,
    [list_b.append(int(input())) for b in range(3)]   # вводимые пользователем

    print('Введите размеры сторон дверного проема: ') # Получает 2 значения
    list_d = list()                                   # размеров дверного проёма,
    [list_d.append(int(input())) for d in range(2)]   # вводимые пользователем

    list_d.append(0)                                  # Выравнивает длины списков
    dim([list_b, list_d])                             # Вызов ф-ции с параметрами в виде двух списков

def dim(list_data):                                   # Ф-ция получает список из двух списков
    int_side = 0                                      # Начальное значение счетчика
    for i in range(len(list_data[0])):                # Формирование 2-х мерной матрицы
        for j in range(len(list_data[1])):            # из списков
            if list_data[1][j] > list_data[0][i]:     # Проверка размеров
                int_side += 1                         # Добавляет к счетчику 1
    if int_side > 2:                                  # Проверяет счетчик, есть ли,
                                                      # как минимум два выполнившихся цсловия
        print('Коробка пройдет!')                     # Печатает, если есть
    else:
        print('Коробка не пройдет!')                  # Печатает, если нет

input_data()                                          # Вызов ф-ции

# #==============================================================================================
# # 10. Можно ли из бревна, имеющего диаметр поперечного сечения D,
# # выпилить квадратный брус шириной A?

import math                                           # Подключаем math

float_d = float(input('Введите диаметр бревна: '))            # Получает диаметр бревна от пользователя
float_a = float(input('Введите ширину квадратного бруса: '))  # Получает ширину бруса от пользователя

def func_sq(d, a):                                    # Ф-ция получает диаметр и ширину
    if math.sqrt(d**2) > math.sqrt(2 * a**2):         # Проверяет возмодность выпиливания
        print('Выпилить можно!')                      # Печатает, если выполняется условие
    else:
        print('Выпилить нельзя!')                     # Печатает, если не выполняется условие

func_sq(float_d, float_a)                             # Вызов ф-ции

# #==============================================================================================
# # 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# # верхнее или нижнее, в купе или боковое.

int_place = input('Введите номер места в вагоне, от 1 до 54: ')
                                                      # Получает строку с номером места
def upper_lower(a):                                   # Ф-ция получает строку
    if int(a) % 2 == 0:                               # Если чётный номер
        str_ul = 'верхнего'                           # Возвращает нужную строку
    else:                                             # Если нечётный номер
        str_ul = 'нижнего'                            # Возвращает нужную строку
    return str_ul                                     # Возвращает выбранную строку

def room_side(a):
    if int(a) > 36:                                   # Если номер больше 36
        str_rs = 'бокового'                           # Возвращает нужную строку
    else:                                             # Если номер меньше 36
        str_rs = 'купейного'                          # Возвращает нужную строку
    return str_rs                                     # Возвращает выбранную строку

upper_lower(int_place)                                # Вызов ф-ции
room_side(int_place)                                  # Вызов ф-ции

print('Вы указали номер', upper_lower(int_place), room_side(int_place), 'места!')
                                                      # Печатает полученные строки
# #==============================================================================================
# # 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# # монетой 2 грн., если это возможно.

float_money = float(input('Введите сумму для размена: '))
                                                      # Получает от пользователя сумму, и преобразовывает во float
list_bank = [500, 100, 10, 2]                         # Список разменных купюр

def exchange(s):                                      # Ф-ция получает переменную
    dict_money = dict()                               # Объявляет словарь
    for i in range(len(list_bank)):                   # Цикл по списку разменных купюр
        float_rem = s % list_bank[i]                  # Получает остаток, и записывает в переменную
        int_res = int(s // list_bank[i])              # Получает целую часть
        if int_res > 0:                               # Если целая часть остаётся:
            dict_money.update({list_bank[i]: int_res})# Добавляет в словарь с ключом купюры
        s = float_rem                                 # Присваивает переменной значение остатка
    if float_rem > 0:                                 # После итераций: Если остаток есть, то:
        print('Размен с остатком!')                   # Возвращает остаток
    else:                                             # Если остатка нет, то:
        print(dict_money)                             # Печатает набранный словарь

exchange(float_money)                                 # Вызов ф-ции

# #==============================================================================================
# # 13. Пользователь вводит число n, программа должна проверить является ли
# # оно простым и сообщить об этом.

int_number = int(input('Введите число: '))            # Получает от пользователя число, преобразовывает
                                                      # строку в int, и присваивает переменной
def simple(num):                                      # Ф-ция получает переменную
    i = num                                           # Определяет количество итераций цикла
    count = 0                                         # Присваивает нулевое значение счётчику
    while i > 0:                                      # Цикл, пока i > 0
        if num % i == 0:                              # Если делится без остатка, то:
            count += 1                                # Добавляет 1 к счётчику
            i -= 1                                    # Отнимает 1 от i
        else:                                         # Если делится с остатком, то:
            i -= 1                                    # Просто, отнимает 1 от i
    if count == 2:                                    # Если счётчик = 2, то:
        print('Введенное число является простым!')    # Печатает, что число - простое
    else:                                             # Если счётчик больше 2-х, то:
        print('Введенное число не является простым!') # Печатает, что число - не простое

simple(int_number)                                    # Вызов ф-ции

# #==============================================================================================
# # 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# # Числа M, a и b вводит пользователь.

int_m = int(input("Введите множитель: "))             # ------------------------
                                                      # Получает строку, преобразовывает в int,
int_min = int(input("Введите начальное значение: "))  # присваивает значение переменной
int_max = int(input("Введите конечное значение: "))   # ------------------------

def tab(m, a, b):                                     # Ф-ция принимает 3 переменных
    for i in range(a, b + 1):                         # Цикл от начального значения до конечного
        print('{} * {} = {}'.format(m, i, m*i))       # Форматированная печать

tab(int_m, int_min, int_max)                          # Вызов ф-ции
------------------------
# #==============================================================================================
# # 15. Дан одномерный массив числовых значений, насчитывающий N
# # элементов. Поменять местами элементы, стоящие на чётных и нечётных
# # местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

int_m = int(input('Введите число элементов массива: '))
                                                      # Получает от пользователя число эелементов массива,
                                                      # преобразовывает в int, и присваивает переменной
list_res = list()                                     # Объявляет список
[list_res.append(input('Введите {}-й элемент: '.format(i + 1))) for i in range(int_m)]
                                                      # Добавляет в список элементы массива int_m раз
print(list_res)                                       # Печатает исходный массив

for i in range(int_m):                                # Цикл по количеству элементов
    if i % 2 == 0 and i + 1 < int_m:                  # Если итерация чётная, и следующий элемент
                                                      # меньше общего кол-ва элементов, то:
        list_res[i], list_res[i + 1] = list_res[i + 1], list_res[i]
                                                      # Меняет элементы местами
print(list_res)                                       # Печатает обновленный список

#==============================================================================================
# 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.

list_str = ['начальное значение', 'конечное значение']# Вспомогательный список
list_id = [int(input('Введите {}: '.format(list_str[id]))) for id in range(2)]
                                                      # Получает 2 значения от пользователя в список
def function16(list_id):                              # Ф-ция принимает список
    list_simple = list()                              # Объявляет список простых чисел
    for el in range(list_id[0], list_id[1] + 1):      # Цикл с переменной el
        counter = 0                                   # Обнуляет счётчик
        tmp_simple = el                               # Присваивает переменной номер итерации
        while tmp_simple:                             # Цикл с переменной
            if el % tmp_simple == 0:                  # Если делится без остатка, то
                counter += 1                          # Прибавляет к счётчику 1
            tmp_simple -= 1                           # Отнимает 1 для следующей итерации while
        if counter == 2:                              # Проверяет счётчик, и если значение = 2, то
            list_simple.append(el)                    # Добавляет простое число в список
    return list_simple                                # Возвращает список простых чисел

print(function16(list_id))                            # Печатает список простых чисел, вызывая функцию
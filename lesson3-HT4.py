# 4. Есть список элементов (могут быть строки, словари, числа и другие типы данных).
# Создать словарь в котором будут ключи имена типов данных и в значениях лежать
# сами значения в списке.
# Пример:
# [1,"2", {"123":123}, [1,2,3,4]]
# На выходе должно быть:
# {'list': [[1,2,3,4]], 'dict':[{"123":123}], 'int': [1], 'str': ["2"]}

list_a = [1,"2", {"123":123}, [1,2,3,4]]
dict_res = dict()

for a in list_a:
    if type(a) == list:
        print(type(a))
        dict_res.update({'list' : a})
    elif type(a) == dict:
        dict_res.update({'dict' : a})
    elif type(a) == int:
        dict_res.update({'int': a})
    elif type(a) == str:
        dict_res.update({'str' : a})
    else:
        dict_res.update({'other type' : a})

print(dict_res)
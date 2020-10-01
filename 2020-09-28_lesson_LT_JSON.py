import os
import json

os.chdir(os.getcwd())


class User:

    list_objects = list()

    def __init__(self, surname, name, int_phone, int_age, *args, **kwargs):
        self.surname = surname
        self.name = name
        self.phone = int_phone
        self.age = int_age
        self.list_objects.append(self)


class Employee(User):

    def __init__(self, surname, name, int_phone, int_age, prof, firm, *args, **kwargs):
        super().__init__(surname, name, int_phone, int_age, *args, **kwargs)
        self.prof = prof
        self.firm = firm


class Student(User):

    def __init__(self, surname, name, int_phone, int_age, university, course, *args, **kwargs):
        super().__init__(surname, name, int_phone, int_age, *args, **kwargs)
        self.university = university
        self.course = course


def write_persons():
    list_dict_persons = list()
    for i in User.list_objects:
        dict_persons = {'surname': i.surname, 'name': i.name, 'phone': i.phone, 'age': i.age}
        if isinstance(i, Employee):
            dict_persons.update({'prof': i.prof,'firm': i.firm})
        if isinstance(i, Student):
            dict_persons.update({'university': i.university, 'course': i.course})
        print('В файл записан экземпляр {} класса {}: '.format(i, type(i)))

        list_dict_persons.append(dict_persons)
    f = open('Persons_Data.txt', 'w')
    f.write(str(list_dict_persons))
    f.close()


def read_persons(file_name):
    f = open(file_name, 'r')
    str_data = str()
    str_end = str()
    for line in f:
        str_data += line[0: len(line) - 1]
        str_end = line[len(line) - 1:]
    str_data += str_end
    f.close()
    list_data = json.loads(str_data.replace("'",'"'))
    try:
        for i in list_data:
            if i.get('surname', 0) != 0 and\
                i.get('name', 0) != 0 and\
                i.get('phone', 0) != 0 and\
                i.get('age', 0) != 0 and\
                i.get('university', 0) != 0 and\
                i.get('course', 0) != 0:
                obj = Student(i.get('surname'), i.get('name'),\
                        i.get('phone'), i.get('age'),\
                        i.get('university'), i.get('course'))
                print('Прочитан из файла, и добавлен новый экземпляр {} класса {}: '.format(obj, type(obj)))
            elif i.get('surname', 0) != 0 and\
                    i.get('name', 0) != 0 and\
                    i.get('phone', 0) != 0 and\
                    i.get('age', 0) != 0 and\
                    i.get('prof', 0) != 0 and\
                    i.get('firm', 0) != 0:
                obj = Employee(i.get('surname'), i.get('name'),\
                        i.get('phone'), i.get('age'),\
                        i.get('prof'), i.get('firm'))
                print('Прочитан из файла, и добавлен новый экземпляр {} класса {}: '.format(obj, type(obj)))
            else:
                obj = User(i.get('surname'), i.get('name'),\
                         i.get('phone'), i.get('age'))
                print('Прочитан из файла, и добавлен новый экземпляр {} класса {}: '.format(obj, type(obj)))
    except AttributeError:
        print('AttributeError')
    print()
    print('Всего в памяти {} экзепляров.'.format(len(User.list_objects)))

u1 = User('Us1', 'Un1', 101, 1)
u2 = User('Us2', 'Un2', 102, 2)
u3 = User('Us3', 'Un3', 103, 3)
e1 = Employee('Es1', 'En1', 201, 11, 'Epr1', 'Ef1')
e2 = Employee('Es2', 'En2', 202, 22, 'Epr2', 'Ef2')
e3 = Employee('Es3', 'En3', 203, 33, 'Epr3', 'Ef3')
s1 = Student('Ss1', 'Sn1', 301, 111, 'Spr1', 'Sf1')
s2 = Student('Ss2', 'Sn2', 302, 222, 'Spr2', 'Sf2')
s3 = Student('Ss3', 'Sn3', 303, 333, 'Spr3', 'Sf3')

write_persons()

read_persons('Persons_Data.txt')
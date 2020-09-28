import os
os.chdir('/media/alex/Work/MY_PYTHON/PycharmProjects/pythonProject/')

list_users_id = list()


class User:
    def __init__(self, surname, name, int_age):
        self.surname = surname
        self.name = name
        self.int_age = int_age
        list_users_id.append(self)

    def user_data_save(self):
        list_to_write = [self.surname, self.name, self.int_age]
        f = open(str.title(self.surname) + '_' + str.title(self.name) + '.txt', 'w')
        for i in list_to_write:
            f.write(str(i) + '\n')
        print('Данные пользователя {} {} успешно записаны в файл {}'.\
              format(self.surname, self.name, str.title(self.surname) + '_' + str.title(self.name)) + '.txt')

    @staticmethod
    def user_data_read(str_file_name):
        try:
            f = open(str_file_name, 'r')
            list_to_read = list()
            for i in f:
                list_to_read.append(i[:len(i) - 1])
            t = User(list_to_read[0], list_to_read[1], list_to_read[2])
            print('Успешно прочитаны данные из файла {}, и создан новый пользователь.'.\
                  format(str_file_name))
            return t
        except FileNotFoundError:
            print('Файл с таким именем не существует.')



u1 = User('S', 'Alex', 10)
u1.user_data_save()

u2 = User.user_data_read('Any_File_Name.txt')
try:
    print('Данные нового пользователя: ', u2.surname, u2.name, u2.int_age)
except AttributeError:
    print('Новый пользователь, по данным файла не был создан.')
print('\nАдреса экземпляров класса:')
print([i for i in list_users_id])


import os


class Sort:
    def __init__(self, name):
        self.name = name

    def sort_to_dirs(self, my_path):
        os.chdir(my_path)
        from os import listdir
        from os.path import isfile, join
        only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

        for i in only_files:
            d = str()
            for j in range(len(i) - 1, -1, -1):
                if i[j] == '.':
                    break
                d += i[j]
            try:
                os.mkdir('_' + d[-1::-1].upper())
                print('Dir created: ', '_' + d[-1::-1].upper())
                os.replace(i, '_' + d[-1::-1].upper() + '/' + i)
                print('File', i, 'was replaced to Dir: ', '_' + d[-1::-1].upper())
            except FileExistsError:
                os.replace(i, '_' + d[-1::-1].upper() + '/' + i)
                print('File', i, 'was replaced to Dir: ', '_' + d[-1::-1].upper())
                continue


p1 = Sort('Test')
p1.sort_to_dirs('/home/alex/Документы/Test')

"""
1. Реализовать класс который принимает путь к файлу
и имеет метод подсчета количества символов,
слов и предложений в файле.
"""


class File_Text_Count:
    def __init__(self, file_path):
        self.file_path = file_path

    def s_count(self):
        f = open(self.file_path, 'r')
        print(f.read())
        f = open(self.file_path, 'r')
        str_file = str()
        str_end = str()
        for line in f:
            str_file += line[0: len(line) - 2]
            str_end = line[len(line) - 2: len(line)]
        str_file += str_end + ' '
        count_symbol = len(str_file)
        count_sentence = 0
        count_words = 0
        for i in range(len(str_file)):
            if str_file[i] == '.':
                count_sentence += 1
            elif str_file[i] == ' ':
                count_words += 1
        print('\nВ файле насчитывается {} пердложений, {} слов, и {} символов.'.\
              format(count_sentence, count_words, count_symbol))


f1 = File_Text_Count('/media/alex/Work/MY_PYTHON/PycharmProjects/pythonProject/AllTemp.py')

f1.s_count()
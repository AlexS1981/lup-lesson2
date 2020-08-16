# Программа по вычислению факториала
# с циклов while

int_number = int(input('Number: '))
int_factorial = 1
int_i = 1
while int_i < int_number:
    int_i += 1
    int_factorial *= int_i
print(int_factorial)


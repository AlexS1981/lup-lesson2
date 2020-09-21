new_id = list()


class A:
    def __init__(self, a):
        self.a = a
        new_id.append(self)

    @staticmethod
    def pr():
        for i in new_id:
            print(i, i.a)
        print()


class B:
    def __init__(self, b):
        self.b = b
        new_id.append(self)

    @staticmethod
    def pr():
        for i in new_id:
            # print(i, i.a)
            print(i, i.b)
            """
            В каждом классе должен быть свой список адресов экземпляров,
            а общий список адресов не должен использоваться в цикле, т. к.
            цикл выполняется по атрибуту, который объявлен в одном классе,
            а в общем списке адресов перечисляются адреса разных классов,
            в которых этот атрибут мог и не объявляться.
            """
        print()

a1 = A('_1')
a2 = A('_2')
B.pr()
b1 = B('_3')
b2 = B('_4')
B.pr()
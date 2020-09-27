"""
Программа разработана только для типа ЧС - пожар
(коды 10210, 10212, 10213, 10231 - 10234), но с
написаным алгоритмом общей классификацией ЧС, по коду.
"""
class Emergency:
    """
    Содержит: тип ЧС (пожар, наводнение...),
    характер (природный или техногенный),
    уровень (международный, государственный,
    региональный, местный, объектовый)
    """
    def __init__(self, e_type, nature, level):
        self.e_type = e_type
        self.nature = nature
        self.level = level

#    def set_emergency_code(self):
        """
        Читает из файла форматированный текст классификатора ЧС
        По данным пользователя устанавливается характер и уровень,
        и формируется код ЧС.
        """
        print('Характер и уровень ЧС.')
        print('Код ЧС')


class Emergency_Navigation:
    """
    Содержит связку адресов объектов с их
    координатами, и выполняет доп. ф-ции с
    геометрическими расчетами по навигации.
    """
    def __init__(self, address, district, coordinates):
        self.address = address
        self.district = district
        self.coordinates = coordinates

class Department_SESU:
    """
    Содержит адреса частей МЧС, районы закрепления
    частей, и код их аккредитации по количеству персонала
    и комплектации оборудования для пожаротушения.
    """
    def __init__(self, d_address, d_districts, d_code):
        self.d_address = d_address
        self.d_districts = d_districts
        self.d_code = d_code


class Dep_Code(Department_SESU):
    """
    Содержит персонал и след. автомобили:
    быстрого реагирования;
    с емкостью;
    с лестницей 1;
    с лестницей 2;
    с хим. реактивами
    """
    def __init__(self, d_address, d_districts, d_code, staff, num_car_1,\
                 num_car_2, num_car_3, num_car_4, num_car_5):
        Department_SESU.__init__(self, d_address, d_districts, d_code)
        self.staff = staff
        self.num_car_1 = num_car_1
        self.num_car_2 = num_car_2
        self.num_car_3 = num_car_3
        self.num_car_4 = num_car_4
        self.num_car_5 = num_car_5


class Emergency_Object:
    """
    Содержит тип объекта и его адрес
    """
    def __init__(self, obj_type, address):
        self.obj_type = obj_type
        self.address = address


class Vehicle(Emergency_Object):
    """
    Содержит данные о ТС
    """
    def __init__(self, obj_type, address, v_num_people,\
                 v_weight, v_movement, v_cargo_hazard):
        Emergency_Object.__init__(self, obj_type, address)
        self.v_num_people = v_num_people
        self.v_weight = v_weight
        self.v_movement = v_movement
        self.v_cargo_hazard = v_cargo_hazard


class Building(Emergency_Object):
    """
    Содержит данные об объекте строительства
    """
    def __init__(self, obj_type, address, b_num_people, b_purpose, b_materials, b_storeys):
        Emergency_Object.__init__(self, obj_type, address)
        self.b_num_people = b_num_people
        self.b_purpose = b_purpose
        self.b_materials = b_materials
        self.b_storeys = b_storeys


class Probability(Emergency_Navigation):
    """
    Содержит статистику пожаров, хранит ее в файле, и производит
    вычисления вероятности пожара, по этим данным
    (факторы: день недели, время суток и т.д.)
    """
    def __init__(self, address, district, coordinates, date, e_code):
        Emergency_Navigation.__init__(self, address, district, coordinates)
        self.date = date
        self.e_code = e_code

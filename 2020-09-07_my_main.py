# class Container:
# 	def __init__(self, *args, **kwargs):
# 		self.__args = args
# 		self.__kwargs = kwargs
#
# 	def show_items(self):
# 		print("Args: {}".format(self.__args))
# 		print("Kwargs: {}".format(self.__kwargs))
#
# 	def add_items(self, *args, **kwargs):
# 		result_list = list(self._args)
# 		result_list.extend(args)
# 		self.__args = tuple(result_list)
# 		self.__kwargs.update(kwargs)
#
#
# def xy_points (xy_dict):
#   list_res = list()
#   for i in range(len(xy_dict["features"]):
#     list_res.append(xy_dict["features"]["geometry"])


# Реализовать функцию которая принимает словарь вида:

new_xy_dict =\
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              69.2578125,
              30.031055426540206
            ],
            [
              72.2900390625,
              30.031055426540206
            ],
            [
              72.2900390625,
              31.50362930577303
            ],
            [
              69.2578125,
              31.50362930577303
            ],
            [
              69.2578125,
              30.031055426540206
            ]
          ]
        ]
      }
    },

    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              73.037109375,
              31.16580958786196
            ],
            [
              74.3994140625,
              31.16580958786196
            ],
            [
              74.3994140625,
              31.87755764334002
            ],
            [
              73.037109375,
              31.87755764334002
            ],
            [
              73.037109375,
              31.16580958786196
            ]
          ]
        ]
      }
    },

    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Point",
        "coordinates": [
          73.4326171875,
          30.600093873550072
        ]
      }
    }
  ]
}


def dsa(xy_dict):
  list_res = list()
  for i in xy_dict["features"]:
    if i["geometry"]["type"] == "Polygon":
      for j in range(len(i["geometry"]["coordinates"][0])):
        if type(i["geometry"]["coordinates"][0][j][0]) and type(i["geometry"]["coordinates"][0][j][1]) == float:
          list_res.append(i["geometry"]["coordinates"][0][j])
        else:
          print('No geometry!')
    elif i["geometry"]["type"] == "Point":
      if type(i["geometry"]["coordinates"][0]) and type(i["geometry"]["coordinates"][1]) == float:
        list_res.append(i["geometry"]["coordinates"])
      else:
        print('No geometry!')
    else:
      return "Geometry type error!"
  return list_res


# for i in len(new_xy_dict["features"]["geometry"]["coordinates"]):
#   try:
#     float(new_xy_dict["features"]["geometry"]["coordinates"])
#   except ValueError:

print(dsa(new_xy_dict))
#
# Функция должна вернуть все координаты в виде списка т.е [[73.037109375, 31.16580958786196], [74.3994140625, 31.87755764334002]...].
# Так же функция должна валидировать входной словарь и если что-то введено неправильно - вернуть сообщение об этом.

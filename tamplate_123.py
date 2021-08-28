##from bot import bot
#bot.polling(none_stop=True)
# from bot import bot
#
# bot.polling(none_stop=True)
#
# class Point:
#     def __init__(self, weight_lenght_height = [10, 10, 10]):
#         self.weight_lenght_height = weight_lenght_height
#
#
#     def reLoad(self, weight_lenght_height, aaa = 10, bbb = 20, ccc = 30):
#         weight_lenght_height[0] += aaa
#         weight_lenght_height[1] += bbb
#         weight_lenght_height[2] += ccc
#         tup = tuple(weight_lenght_height)
#         return tup
#
#
# a = int(input('weight = '))
# b = int(input('lenght = '))
# c = int(input('height = '))
#
# aaa = int(input('REweight = '))
# bbb = int(input('Relenght = '))
# ccc = int(input('REheight = '))
#
# coords1 = Point()
# coords2 = Point([c, b, a])
# coords3 = Point([c, a, b])
# coords40 = Point([100, 200, 300])
#
#
# tuple_coords1 = coords1.reLoad(coords1.weight_lenght_height)
# tuple_coords2 = coords2.reLoad(coords2.weight_lenght_height, ccc, bbb, aaa)
# tuple_coords3 = coords3.reLoad(coords3.weight_lenght_height, ccc, aaa, bbb)
# tuple_coords40 = coords40.reLoad(coords40.weight_lenght_height, aaa + 1000, bbb + 2000, ccc + 3000)
#
# print(tuple_coords1, type(tuple_coords1))
# print(tuple_coords2, type(tuple_coords2))
# print(tuple_coords3, type(tuple_coords3))
# print(tuple_coords40, type(tuple_coords40))
#
# x = True
# while x:
#     value =  int(input('please enter your number '))
#     if not value % 7:
#         print('This number is a multiple of seven')
#         x = False
#     else:
#         print('This number is NOT a multiple of seven')
#         yes_no = input('Press \"Y\" if you want continue , or\"N\" if you want break search ')
#         if yes_no.lower() == 'y':
#             continue
#         else:
#             break
# else:
#     print('you found the required number')
# print('End')
#
# class Cat:
#
#     def __init__(self, name, breed = 'dvorovoy', age = 13, color = 'dirty white'):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.color = color
#
#
#
# mursic = Cat('Mursic',)
# manan = getattr(mursic, 'name')
# mana = getattr(mursic, 'breed')
# man = getattr(mursic, 'age')
# ma = getattr(mursic, 'color')
# print(manan, mana, man, ma, sep='\n')

# from datetime import datetime as dt
#
# class Player:
#
#     __LVL, __HEALTH = 1, 100
#     __slots__ = ['__lvl', '__health', '__born']
#
#     def __init__(self):
#         __lvl = Player.__LVL
#         __health = Player.__HEALTH
#         __born = dt.now()
#
#     def get_lvl(self):
#         return self.__lvl
#
#     def set_lvl(self, numeric):
#         self.__lvl += numeric
#
#
# x = Player()
# print(x.get_lvl())
#
#
# class Animal:
#     # !! Your home task
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Hello I\'m - ', self.name)
#
# class Dog(Animal):
#     def __init__(self, name, ear = 2):
#         super(Dog, self).__init__(name)
#         self.ear = ear
#
#     def baww(self):
#         print('baw baw baw')
#
# class Fish(Animal):
#     def __init__(self, name, tail):
#         super(Fish, self).__init__(name)
#         self.tail = tail
#
#     def boolbool(self):
#         print('Bool bool')
#
#
#
#
# nemo = Fish('Nemo', 2.5) # Nemo_001
# nemo.boolbool()
# nemo.speak()
#
# sharic = Dog('ShariC', 4) # Sharic_001
# sharic.baww()
# sharic.speak()
from bot import bot

bot.polling(none_stop=True)

# class Car:
#     brand = 'BMW'
#     model = 'X-5'
#     engine = 4.4
#     def setSpeed(self,brand, model, engine):
#         self.brand = brand
#         self.model = model
#         self.engine = engine
#
#
# volga = Car()
# volga.setSpeed('GAZ','2401', 2.4)
# print(volga.brand)
# print(volga.model)
# print(volga.engine)
# volvo = Car()
# volvo.setSpeed('VOLVO', '850 GTL', 2.5)
# print(volvo.brand)
# print(volvo.model)
# print(volvo.engine)
# bmw = Car()
# print(bmw.brand)
# print(bmw.model)
# print(bmw.engine)

# def square(x):
#     print('Квадрат чистла', x, '=', x**2)
# def multyply(x, y):
#     print(x, '*', y, '=',x * y)
# def even(x):
#     if not x % 2:
#         print(x, 'четное')
#     else:
#         print(x, 'Нечетное')
#
# square(10)
# multyply(3,15)
# for i in range(1,101):
#     even(i*i)
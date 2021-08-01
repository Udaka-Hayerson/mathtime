# from bot import bot
#
# bot.polling(none_stop=True)
#
from mathuynya import Multiply, HargMultiply, DivideUp, DivideUpHard, Plus, Minus, int_time

plus_obj = Plus(int_time)
print(plus_obj.plus_task())

minus_obj = Minus(int_time)
print(minus_obj.minus_task())

divide_up_obj = DivideUp(int_time)
print(divide_up_obj.divide_up_task())

divide_uphard_obj = DivideUpHard(int_time)
print(divide_uphard_obj.divide_up_taskhard())

multiply_obj = Multiply(int_time)
print(multiply_obj.multiply_task())

hargmultiply_obj = HargMultiply(int_time)
print(hargmultiply_obj.multiply_taskhard())
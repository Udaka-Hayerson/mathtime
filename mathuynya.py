# from datetime import datetime
# import random
#
#
# class GetIntTime:
#     def __init__(self):
#         self.str_newtime = str(datetime.now().time())[0:5]      # обрезаем лишние секунди и милисекунды
#         self.format_str_newtime = self.str_newtime.replace(':', '')  # удаляем двоеточие
#         self.int_time = int(self.format_str_newtime)
#
# class Multiply:
#     def __init__(self):
#         self.time = GetIntTime().int_time
#
#     def multiply_task(self):
#         for i in range(9, 1, -1):
#             n = self.time / i                  # делим время как число на числа от 10
#             if n != 0 and n != 1 and not n % 1:  # если число натуральное
#                 return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя
#             else:
#                 for j in range(9, 0, -1):
#                     n = (self.time - j) / i
#                     if n != 0 and n != 1 and not n % 1:
#                         return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя
#
# class HargMultiply:
#     def __init__(self):
#         self.time = GetIntTime().int_time
#
#     def multiply_taskhard(self):
#         for i in range(99, 20, -1):
#             n = self.time / i                  # делим время как число на числа от 99 до 21
#             if n != 0 and n != 1 and not n % 1:           # если число натуральное не равно нулю и единице
#                 return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя
#
#             else:
#                 for j in range(99, 20, -1):
#                     n = (self.time - j) / i                      # отнимаем от времени число от 99 до 21 и делим на числа от 99 до 21
#                     if n != 0 and n != 1 and not n % 1:                 # если число натуральное не равно нулю и единице
#                         return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя
#
# class DivideUp:
#     def __init__(self):
#         self.time = GetIntTime.int_time
#
#     def divide_up_task(self):
#         p = random.randint(2, 10)
#         n = self.time * p
#         return f'{n} ÷ {p} = '
#
# class DivideUpHard:
#     def __init__(self):
#         self.time = GetIntTime.int_time
#
#     def divide_up_taskhard(self):
#         p = random.randint(2, int(self.time / 2))
#         n = self.time * p
#         return f'{n} ÷ {p} = '
#
#
# class Plus:
#     def __init__(self):
#         self.time = GetIntTime.int_time
#
#     def plus_task(self):
#         p = random.randint(0, int(self.time / 2))
#         n = self.time - p
#         return f'{n} + {p} = '
#
#
# class Minus:
#     def __init__(self):
#         self.time = GetIntTime.int_time
#
#     def minus_task(self):
#         p = random.randint(0, int(self.time))
#         n = self.time + p
#         return f'{n} - {p} = '
import copy
from datetime import datetime
import random
new_dt = str(datetime.now().time())   # получаем время вформате xx.xx.xx.xxxxx и преобразуем в строку
str_newdt = new_dt[0:5]               # обрезаем лишние секунди и милисекунды
f_s_ndt = str_newdt.replace(':', '')  # удаляем двоеточие
int_time = int(f_s_ndt)               # преобразуем в Integer
str_otvet = ''
n = 0
comparison = ''

def deep_copy_result(result):
    asnw_copy = copy.deepcopy(str(result))
    return asnw_copy


class Multiply:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def multiply_task(self):
        for i in range(9, 1, -1):
            n = self.time / i                  # делим время как число на числа от 10
            if n != 0 and n != 1 and not n % 1:  # если число натуральное
                return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя
            else:
                for j in range(9, 0, -1):
                    n = (self.time - j) / i
                    if n != 0 and n != 1 and not n % 1:
                        return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя

class HargMultiply:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def multiply_taskhard(self):
        for i in range(99, 20, -1):
            n = self.time / i                  # делим время как число на числа от 99 до 21
            if n != 0 and n != 1 and not n % 1:           # если число натуральное не равно нулю и единице
                return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя

            else:
                for j in range(99, 20, -1):
                    n = (self.time - j) / i                      # отнимаем от времени число от 99 до 21 и делим на числа от 99 до 21
                    if n != 0 and n != 1 and not n % 1:                 # если число натуральное не равно нулю и единице
                        return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя

class DivideUp:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def divide_up_task(self):
        p = random.randint(2, 10)
        n = self.time * p
        return f'{n} ÷ {p} = '

class DivideUpHard:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def divide_up_taskhard(self):
        p = random.randint(2, int(self.time / 2))
        n = self.time * p
        return f'{n} ÷ {p} = '


class Plus:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def plus_task(self):
        p = random.randint(0, int(self.time / 2))
        n = self.time - p
        return f'{n} + {p} = '


class Minus:
    comparison = deep_copy_result(int_time)
    def __init__(self, time):
        self.time = int_time

    def minus_task(self):
        p = random.randint(0, int(self.time))
        n = self.time + p
        return f'{n} - {p} = '
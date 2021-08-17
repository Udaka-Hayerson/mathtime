from datetime import datetime
import random


def get_int_time():         #  Функиция , задача которой формировать обьект для матиматических функций
    str_newtime = str(datetime.now().time())[0:5]              # обрезаем лишние секунди и милисекунды
    format_str_newtime = str_newtime.replace(':', '')          # удаляем двоеточие
    task_hint = 0
    for i in format_str_newtime:
        task_hint += int(i) #  taskHint -  подсказка для пользователя. - ответом на задачку будет ,
                            # сумма времени как целого числа и суммы его отдельных цифр
    int_time = int(format_str_newtime)
    getinttime = int_time + task_hint
    return getinttime


def multiply_task(time):
    for i in range(9, 1, -1):
        n = time / i                  # делим время как число на числа от 10
        if n != 0 and n != 1 and not n % 1:  #
            return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя
        else:
            for j in range(9, 0, -1):
                n = (time - j) / i
                if n != 0 and n != 1 and not n % 1:
                    return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя

def multiply_taskhard(time):
    for i in range(99, 20, -1):
        n = time / i                  # делим время как число на числа от 99 до 21
        if n != 0 and n != 1 and not n % 1:           # если число натуральное не равно нулю и единице
            return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя

        else:
            for j in range(99, 20, -1):
                n = (time - j) / i                      # отнимаем от времени число от 99 до 21 и делим на числа от 99 до 21
                if n != 0 and n != 1 and not n % 1:                 # если число натуральное не равно нулю и единице
                    return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя

def divide_up_task(time):
    p = random.randint(2, 10)
    n = time * p
    return f'{n} ÷ {p} = '

def divide_up_taskhard(time):
    p = random.randint(2, int(time / 2))
    n = time * p
    return f'{n} ÷ {p} = '

def plus_task(time):
    p = random.randint(0, int(time / 2))
    n = time - p
    return f'{n} + {p} = '

def minus_task(time):
    p = random.randint(0, int(time))
    n = time + p
    return f'{n} - {p} = '
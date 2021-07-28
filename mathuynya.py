from datetime import datetime

new_dt = str(datetime.now().time())   # получаем время вформате xx.xx.xx.xxxxx и преобразуем в строку
str_newdt = new_dt[0:5]               # обрезаем лишние секунди и милисекунды
f_s_ndt = str_newdt.replace(':', '')  # удаляем двоеточие
int_time = int(f_s_ndt)               # преобразуем в Integer
str_otvet = ''
n = 0
print('control  ', int_time, int_time/2)  # контрольная проверка - в готовом варианте не требуется
print('запуск программы! это важно') # лог для запуска программы

def task_generator(int_time):
    for i in range(9, 1, -1):
        n = int_time / i                  # делим время как число на числа от 10
        if n != 0 and n != 1 and not n % 1:  # если число натуральное
            return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя
        else:
            for j in range(9, 0, -1):
                n = (int_time - j) / i
                if n != 0 and n != 1 and not n % 1:
                    return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя


def task_generator_hard(int_time):
    for i in range(99, 20, -1):
        n = int_time / i                  # делим время как число на числа от 99 до 21
        if n != 0 and n != 1 and not n % 1:           # если число натуральное не равно нулю и единице
            return f'{int(n)} * {i} = '  # выводим на экран задачку для пользователя

        else:
            for j in range(99, 20, -1):
                n = (int_time - j) / i                      # отнимаем от времени число от 99 до 21 и делим на числа от 99 до 21
                if n != 0 and n != 1 and not n % 1:                 # если число натуральное не равно нулю и единице
                    return f'{int(n)} * {i} + {j} = '  # выводим на экран задачку для пользователя

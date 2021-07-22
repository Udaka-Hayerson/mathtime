from datetime import datetime
from random import random
new_dt = str(datetime.now().time())   # получаем время вформате xx.xx.xx.xxxxx и преобразуем в строку
str_newdt = new_dt[0:5]               # обрезаем лишние секунди и милисекунды
f_s_ndt = str_newdt.replace(':', '')  # удаляем двоеточие
int_time = int(f_s_ndt)               # преобразуем в Integer
str_otvet = ''
n = 0

print('control  ', int_time, int_time/2)  # контрольная проверка - в готовом варианте не требуется

def task_generator(int_time):
    for i in range(9, 1, -1):
        n = int_time / i                  # делим время как число на числа от 10
        if not n % 1:                     #  если число натуральное
            otvet = int(input(f'{int(n)} * {i} = '))  # выводим на экран задачку для пользователя
            if otvet == int_time:         # определяем  правельно ли пользователь решил задачу
                str_otvet = 'My congratulations - your time: ' + new_dt
                return str_otvet
            else:
                str_otvet = 'You counted incorrectly or guessed wrong))'
                return str_otvet
        else:
            for j in range(9, 0, -1):
                n = (int_time - j) / i
                if not n % 1:
                    otvet = int(input(f'{int(n)} * {i} + {j} = '))   # выводим на экран задачку для пользователя
                    if otvet == int_time:   # определяем  правельно ли пользователь решил задачу
                        str_otvet = 'My congratulations - your time: ' + new_dt
                        return str_otvet
                    else:
                        str_otvet = 'You counted incorrectly or guessed wrong))'
                        return str_otvet

def task_generator_hard(int_time):
    for i in range(99, 20, -1):
        n = int_time / i                  # делим время как число на числа от 99 до 21
        if n != 0 and n != 1 and not n % 1:           # если число натуральное не равно нулю и единице
            otvet = int(input(f'{int(n)} * {i} = '))  # выводим на экран задачку для пользователя
            if otvet == int_time:         # определяем  правельно ли пользователь решил задачу
                str_otvet = 'My congratulations - your time: ' + new_dt
                return str_otvet
            else:
                str_otvet = 'You counted incorrectly or guessed wrong))'
                return str_otvet
        else:
            for j in range(99, 20, -1):
                n = (int_time - j) / i                      # отнимаем от времени число от 99 до 21 и делим на числа от 99 до 21
                if n != 0 and n != 1 and not n % 1:                 # если число натуральное не равно нулю и единице
                    otvet = int(input(f'{int(n)} * {i} + {j} = '))  # выводим на экран задачку для пользователя
                    if otvet == int_time:                   # определяем  правельно ли пользователь решил задачу
                        str_otvet = 'My congratulations - your time: ' + new_dt
                        return str_otvet
                    else:
                        str_otvet = 'You counted incorrectly or guessed wrong))'
                        return str_otvet

print(task_generator(int_time))
print(task_generator_hard(int_time))

simple = int(input('''Enter a number from 1 to 10 if you want a simpler problem
or enter more than 10 if you want a more difficult problem  : ''').lower())
# введите число от 1 до 10 если хотите задачку попроще или
# введите больше 10 если хотите задачку посложнее
yes_no = input('write \"yes\" if you want to continue  :').lower()

if simple <= 10:
    while yes_no == 'yes':
        task_generator(int_time)
        yes_no = input('write \"yes\" if you want to continue : ').lower()
elif simple > 10:
    while yes_no == 'yes':
        task_generator_hard(int_time)
        yes_no = input('write \"yes\" if you want to continue : ').lower()

print(' счастливый конец ')
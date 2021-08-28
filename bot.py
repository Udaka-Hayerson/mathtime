# import telebot
# import sqlite3
# from telebot import types
# from mathuynya import get_int_time, multiply_task, multiply_taskhard, divide_up_task, divide_up_taskhard, plus_task, minus_task
# from datetime import datetime
#
# TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
# bot = telebot.TeleBot(TOKEN)
# conn = sqlite3.connect('orders.db')   # -------- создаем базу данных для бота в которую будет записывать данные
# cur = conn.cursor()
# cur.execute('')                       # -------- пользователя и ответ на текущую задачу функция (def dataBase)на строке
#
# # lol
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     multiply = types.KeyboardButton('×××')
#     divide_up = types.KeyboardButton('÷÷÷')
#     plus = types.KeyboardButton('+++')
#     minus = types.KeyboardButton('---')
#     multiplyharg = types.KeyboardButton('ha×××rd')
#     divide_uphard = types.KeyboardButton('ha÷÷÷rd')
#     markup.add(multiply, divide_up, plus, minus, multiplyharg, divide_uphard)
#     bot.send_message(message.chat.id, 'Приветствую Юдзьверь. Я Матбот, бот для любителей себя помучать математикой',
#                      parse_mode='html', reply_markup=markup)
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, 'Я ничем не могу тебе помочь , можешь поныть как тебе тяжело жить но получишь '
#                                       'ты только новую задачку , и проблем станет на одну больше', parse_mode='html')
#
# @bot.message_handler(content_types=['text'])
# def keyboard_handler(message):
#     time_args = get_int_time()   # кроме генерации аргумента для функций
#     requests_usr = ''
#     guesses_or_knows = str(get_int_time())
#     if message.chat.type == 'private':
#         if message.text == '×××':
#             requests_usr = multiply_task(time_args)
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '÷÷÷':
#             requests_usr = divide_up_task(time_args)
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '+++':
#             requests_usr = plus_task(time_args)
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '---':
#             requests_usr = minus_task(time_args)
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == 'ha×××rd':
#             requests_usr = multiply_taskhard(time_args)
#             bot.send_message(message.chat.id,requests_usr, parse_mode='html')
#         elif message.text == 'ha÷÷÷rd':
#             requests_usr = divide_up_taskhard(time_args)
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif guesses_or_knows in message.text:
#             congratulations = str(datetime.now().time())
#             bot.send_message(message.chat.id, 'Ты БАТЯ на математической Олимпиаде  ' + congratulations, parse_mode='html')
#         else:
#             bot.send_message(message.chat.id, 'Либо ты НЕ КРАСАВА и НЕ CongratuletionS ,,, либо ты слишком много от '
#                                               'меня хочешь', parse_mode='html')
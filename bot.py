# import telebot
# from telebot import types
# from mathuynya import Multiply, HargMultiply, DivideUp, DivideUpHard, Plus, Minus, GetIntTime
# from datetime import datetime
#
# TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
# bot = telebot.TeleBot(TOKEN)
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
#     guessed_or_knew = str(GetIntTime().int_time)
#     #time_args = GetIntTime().int_time
#     if message.chat.type == 'private':
#         if message.text == '×××':
#             multiply_obj = Multiply()
#             requests_usr = multiply_obj.multiply_task()
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '÷÷÷':
#             divide_up_obj = DivideUp()
#             requests_usr = divide_up_obj.divide_up_task()
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '+++':
#             plus_obj = Plus()
#             requests_usr = plus_obj.plus_task()
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == '---':
#             minus_obj = Minus()
#             requests_usr = minus_obj.minus_task()
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == 'ha×××rd':
#             hargmultiply_obj = HargMultiply()
#             requests_usr = hargmultiply_obj.multiply_taskhard()
#             bot.send_message(message.chat.id,requests_usr, parse_mode='html')
#         elif message.text == 'ha÷÷÷rd':
#             divide_uphard_obj = DivideUpHard()
#             requests_usr = divide_uphard_obj.divide_up_taskhard()
#             bot.send_message(message.chat.id, requests_usr, parse_mode='html')
#         elif message.text == guessed_or_knew:
#             congratulations = str(datetime.now().time())
#             bot.send_message(message.chat.id, 'Ты БАТЯ на математической Олимпиаде  ' + congratulations, parse_mode='html')
#         else:
#             bot.send_message(message.chat.id, 'Либо ты НЕ КРАСАВА и НЕ CongratuletionS ,,, либо ты слишком много от'
#                                           ' меня хочешь', parse_mode='html')
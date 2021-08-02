import telebot
from telebot import types
from mathuynya import deep_copy_result, Multiply, HargMultiply, DivideUp, DivideUpHard, Plus, Minus, int_time

TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Приветствую Юдзьверь. Я Матбот, бот для любителей себя помучать математикой', parse_mode='html', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    multiply = types.KeyboardButton('×××')
    divide_up = types.KeyboardButton('÷÷÷')
    plus = types.KeyboardButton('+++')
    minus = types.KeyboardButton('---')
    multiplyharg = types.KeyboardButton('ha×××rd')
    divide_uphard = types.KeyboardButton('ha÷÷÷rd')

    markup.add(multiply, divide_up, plus, minus, multiplyharg, divide_uphard)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я ничем не могу тебе помочь , можешь поныть как тебе тяжело жить но получишь '
                                      'ты только новую задачку , и проблем станет на одну больше', parse_mode='html')

@bot.message_handler(content_types=['text'])
def keyboard_handler(message, comparison=None):
    if message.chat.type == 'private':
        if message.text == comparison:
            bot.send_message(message.chat.id, 'КРАСАВА МОИ CongratuletionS', parse_mode='html')
        if message.text == '×××':
            comparison = deep_copy_result(int_time)
            multiply_obj = Multiply(int_time)
            requests_usr = multiply_obj.multiply_task()
            bot.send_message(message.chat.id, requests_usr, parse_mode='html')
        elif message.text == '÷÷÷':
            comparison = deep_copy_result(int_time)
            divide_up_obj = DivideUp(int_time)
            requests_usr = divide_up_obj.divide_up_task()
            bot.send_message(message.chat.id, requests_usr, parse_mode='html')
        elif message.text == '+++':
            comparison = deep_copy_result(int_time)
            plus_obj = Plus(int_time)
            requests_usr = plus_obj.plus_task()
            bot.send_message(message.chat.id, requests_usr, parse_mode='html')
        elif message.text == '---':
            comparison = deep_copy_result(int_time)
            minus_obj = Minus(int_time)
            requests_usr = minus_obj.minus_task()
            bot.send_message(message.chat.id, requests_usr, parse_mode='html')
        elif message.text == 'ha×××rd':
            comparison = deep_copy_result(int_time)
            hargmultiply_obj = HargMultiply(int_time)
            requests_usr = hargmultiply_obj.multiply_taskhard()
            bot.send_message(message.chat.id,requests_usr, parse_mode='html')
        elif message.text == 'ha÷÷÷rd':
            comparison = deep_copy_result(int_time)
            divide_uphard_obj = DivideUpHard(int_time)
            requests_usr = divide_uphard_obj.divide_up_taskhard()
            bot.send_message(message.chat.id, requests_usr, parse_mode='html')

#
# plus_obj = Plus(int_time)
# print(plus_obj.plus_task())
#
# minus_obj = Minus(int_time)
# print(minus_obj.minus_task())
#
# divide_up_obj = DivideUp(int_time)
# print(divide_up_obj.divide_up_task())
#
# divide_uphard_obj = DivideUpHard(int_time)
# print(divide_uphard_obj.divide_up_taskhard())
#
# multiply_obj = Multiply(int_time)
# print(multiply_obj.multiply_task())
#
# hargmultiply_obj = HargMultiply(int_time)
# print(hargmultiply_obj.multiply_taskhard())
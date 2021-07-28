import telebot

from mathuynya import task_generator, task_generator_hard, int_time
from judge import verno_neverno

TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Приветствую Юдзьверь. Я Матбот, бот для любителей себя помучать математикой', parse_mode='html')

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, 'Я ничем не могу тебе помочь , можешь поныть как тебе тяжело жить но получишь '
                                      'ты только новую задачку , и проблем станет на одну больше', parse_mode='html')

@bot.message_handler(content_types=['text'])
def lalala(message):
    result = task_generator(int_time)
    #result = 'little big'
    bot.send_message(message.chat.id, result)

import telebot
from prettyprinter import pprint
from mathuynya import task_generator, task_generator_hard, int_time
from judge import verno_neverno
TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    result = task_generator(int_time)
    #result = 'little big'
    bot.send_message(message.chat.id, result)
@bot.message_handler()
def gogogo(message):

verno_neverno(answer, int_time)

    #pprint(message)


# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(mydict)

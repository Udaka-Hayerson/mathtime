import telebot
from prettyprinter import pprint

TOKEN = '1773331772:AAH-JkEcVkl1mqcgXdE5GdiTMrE01C-hhio'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])

def lalala(message):
    bot.send_message(message.chat.id, message.text)
    pprint(message)


# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(mydict)

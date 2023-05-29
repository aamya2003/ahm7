import telebot


bot = telebot.TeleBot("5680344748:AAE4pVXq4nZG0gk8rD2jkSB4Bqh3jtLugEw")
@bot.message_handler()
def rep(message: telebot.types.Message):
    bot.reply_to(message, message.text)


bot.infinity_polling(skip_pending=True)

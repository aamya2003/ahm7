import telebot, time
from flask import Flask
from threading import Thread


bot = telebot.TeleBot("5827485632:AAG50cF0-ImvqUQfzeTgpVogM0ttqvKITK0")
app = Flask("")


@app.route("/")
def home():
    return "<b> hello</b>"


def run():
    app.run(host="0.0.0.0", port=8080)


n = {
    "ا": "أ",
    "ب": "پّـ",
    "ت": "پّـ",
    "ث": "ثـْ",
    "ج": "چـِ",
    "خ": "خـ؟ـ",
    "ح": "حـٌـ",
    "د": "دٕ",
    "ذ": "ذٖ",
    "ص": "صِـ",
    "ض": "ضـ!ـّ",
    "ط": "طٍـ",
    "ظ": "ظـُ",
    "ر": "رٕ",
    "ز": "زٔ",
    "ف": "ڤـُ",
    "س": "سـٍ",
    "ي": "يـْ",
    "ن": "ننـٍ",
    "ق": "قـُ",
    "ل": "لـ؟ـِ",
    "ك": "گـ",
    "و": "ؤّ",
    "ه": "ه‍ـ",
}


@bot.message_handler()
def ReplyTo(message: telebot.types.Message):
    text = message.text
    mkTns = text.maketrans(n)

    Result = text.translate(mkTns)
    time.sleep(1)
    bot.reply_to(message, Result)


def keep_alive():
    t = Thread(target=run)
    t.start()


keep_alive()

print("Working ...")
bot.infinity_polling(skip_pending=True)

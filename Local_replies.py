import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling
import random


def LOCALREOLIES(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text

    if msg_text == show_bot_name() and check_group(chat_id):
        rbots = [
            "تفضل؟",
            "عيونه",
            "شتريد؟",
            "عوفني طامس وي الحب...",
            "دا ازحف",
            "مالي خلكك بعدين اجي",
        ]
        rp = random.choice(rbots)
        bot.send_message(chat_id, rp, reply_to_message_id=message.id)

    if showGloblaReply(message.text) and check_group(chat_id):
        bot.send_message(
            chat_id, showGloblaReply(message.text), reply_to_message_id=message.id
        )

    if f"{chat_id}_{message.text}" in shelve.open(Reps_name_file) and check_group(
        chat_id
    ):
        All = show_rep_info(message.chat.id, message.text)
        Type_reply_return(All, message)

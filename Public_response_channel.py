from telebot import *
from telebot.types import *
from time import sleep, time
from database_main import *
from time import sleep
import telebot, time
from time import time
from telebot import types
from functions_to_my_bots import *
import messagesBots


def Control_public_response_channel(message: Message):
    if not message.reply_to_message:
        if ":" in message.text:
            msg = message.text.split(":")
            if len(msg) > 1:
                m1 = msg[0].strip()
                m2 = " ".join(msg[1:])
                Add_general_response_to_the_bot(m1, m2)
                mm = bot.send_message(
                    message.chat.id, "تم حفظ الرد!", reply_to_message_id=message.id
                )
                sleep(4)
                try:
                    bot.delete_message(message.chat.id, mm.id)
                except:
                    pass

        if "مسح الردود" in message.text:
            mm = bot.send_message(
                message.chat.id, "تم مسح جميع الردود", reply_to_message_id=message.id
            )
            DelAll_general_response_from_the_bot
            sleep(4)
            try:
                bot.delete_message(message.chat.id, mm.id)
                bot.delete_message(message.chat.id, message.id)
            except:
                pass

        if len(message.text.split(" ")) > 1 and message.text.split(" ")[0] == "عرض":
            bn = bot.send_message(
                message.chat.id,
                str(
                    "<<<".join(
                        Display_generic_response_to_the_bot(
                            " ".join(message.text.split(" ")[1:])
                        )
                    )
                ),
            )
            sleep(5)
            try:
                bot.delete_message(message.chat.id, message.id)
                bot.delete_message(message.chat.id, bn.id)
            except:
                pass
    else:
        if message.text == "مسح":
            if ":" in message.text:
                msg = message.reply_to_message.text.split(":")

                Del_general_response_fromBOT(msg[0].strip())
            bot.delete_message(message.chat.id, message.reply_to_message.id)
            sleep(3)
            bot.delete_message(message.chat.id, message.id)

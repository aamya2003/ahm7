import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling


def Upload_and_download(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text

    if (
        msg_text in ["رفع الادمينه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        bot_stst = bot.get_chat_member(chat_id, user_.id).status

        if user_.id == My_id or bot_stst == "creator":
            bot.send_message(
                chat_id, "تم رفع الادمينة بنجاح", reply_to_message_id=message.id
            )
            Automatic_lift(chat_id)
        else:
            bot.send_message(
                chat_id,
                "عذرا هذا الامر يخص المالك والمطور فقط",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["تنزيل الكل", "تنزيل جميع الرتب"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        bot_stst = bot.get_chat_member(chat_id, user_.id).status

        if user_.id == My_id or bot_stst == "creator":
            bot.send_message(
                chat_id, "تم تنزيل جميع الرتب", reply_to_message_id=message.id
            )
            Download_all_ranks(chat_id)
        else:
            bot.send_message(
                chat_id,
                "عذرا هذا الامر يخص المالك والمطور فقط",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["م", "مميز", "رفع مميز"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "distinct", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["اد", "ادمن", "رفع ادمن"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "admin", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["مد", "مدير", "رفع مدير"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "reeve", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["منشئ ثانوي", "رفع منشئ ثانوي"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "creator2", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["من", "منشئ", "رفع منشئ"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "creator", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["مالك ثانوي", "رفع مالك ثانوي"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "owner2", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["مالك", "رفع مالك"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "owner", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["مطور ثانوي", "رفع مطور ثانوي"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "devloper2", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["مط", "مطور", "رفع مطور "]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = promotions_function(message, "devloper", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل مميز"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "distinct", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل ادمن"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "admin", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل مدير"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "reeve", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل منشئ ثانوي"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "creator2", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل منشئ"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "creator", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل مطور ثانوي"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "devloper2", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تنزيل مطور"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "devloper", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

    if (
        msg_text in ["تك", "تنزيل من كل الرتب"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            nm = download_function(message, "tk", My_id)
            bot.send_message(chat_id, nm, reply_to_message_id=message.id)

        else:
            pass

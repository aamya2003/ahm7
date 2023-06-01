import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
import messagesBots

# bot = telebot.TeleBot("6160347428:AAFeSLUve3VIaJBfkdqFn7CEdzHpx3kkamU")


button1 = InlineKeyboardButton("- م1", callback_data="bc1")
button2 = InlineKeyboardButton("- م2", callback_data="bc2")
button3 = InlineKeyboardButton("- م3", callback_data="bc3")
button4 = InlineKeyboardButton("- اليوتيوب", callback_data="bc4")
button5 = InlineKeyboardButton("- الالعاب", callback_data="bc5")

raw1 = [button1, button2]
raw2 = [button3]
raw3 = [button4, button5]

keyboard = [raw1, raw2, raw3]


def MyBelowListmrk(keyboard):
    if Ischannell() != "None":
        ch = bot.get_chat(Ischannell())
        keyboard.append(
            [InlineKeyboardButton(text=ch.title, url="https://t.me/" + ch.username)]
        )


MyBelowListmrk(keyboard)


board = InlineKeyboardMarkup(keyboard)

Com_id_us = ""


def cmdText(message: Message):
    global Com_id_us
    msg_text = message.text
    chat_id = message.chat.id
    user_ = message.from_user

    if (
        msg_text in ["الاوامر"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                messagesBots.msgCmd,
                reply_markup=board,
            )

        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if msg_text in ["م1"] and Compulsory_subscription(message) and check_group(chat_id):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                M1,
                reply_markup=Bottom_channel_link(),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if msg_text in ["م2"] and Compulsory_subscription(message) and check_group(chat_id):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                M2,
                reply_markup=Bottom_channel_link(),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )
    if msg_text in ["م3"] and Compulsory_subscription(message) and check_group(chat_id):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                M3,
                reply_markup=Bottom_channel_link(),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )
    if (
        msg_text in ["م4", "اليوتيوب"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                M4,
                reply_markup=Bottom_channel_link(),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["م5", "الالعاب"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            Com_id_us = user_.id
            bot.reply_to(
                message,
                M5,
                reply_markup=Bottom_channel_link(),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )
    return Com_id_us


def cmdQuery(query: CallbackQuery):
    chat_id = query.message.chat.id
    message_id = query.message.id
    user_ = query.from_user

    def IS_adimn(cu):
        if (
            check_group(chat_id)
            # and show_user_info(chat_id, cu)
            # and Get_rank_user(chat_id, cu)
            # not in [
            #     "member",
            #     "distinct",
            #     "blocked",
            #     "muted",
            #     "banned",
            # ]
            and Com_id_us == user_.id
        ):
            return True
        else:
            return False

    if query.data == "bc1" and IS_adimn(query.message.from_user.id):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=messagesBots.M1,
            reply_markup=board,
        )

    elif query.data == "bc2" and IS_adimn(query.message.from_user.id):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=messagesBots.M2,
            reply_markup=board,
        )

    elif query.data == "bc3" and IS_adimn(query.message.from_user.id):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=messagesBots.M3,
            reply_markup=board,
        )

    elif query.data == "bc5" and IS_adimn(query.message.from_user.id):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=messagesBots.M5,
            reply_markup=board,
        )

    elif query.data == "bc4" and IS_adimn(query.message.from_user.id):
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=messagesBots.M4,
            reply_markup=board,
        )

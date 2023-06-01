import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from messagesBots import KitList
import random


def gamesBgr(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text

    if (
        msg_text in ["كت", "كت تويت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if show_group(chat_id)["games"]:
            kitmsg = random.choice(KitList)
            bot.send_message(
                chat_id,
                f"<b> {kitmsg}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["ن", "نقاطي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if show_group(chat_id)["games"]:
            iddd = message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰نقاطك ↫ ❲ {user_bot['points']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["نقاطه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if show_group(chat_id)["games"]:
            iddd = message.reply_to_message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰نقاطه↫ ❲ {user_bot['points']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["رسائلي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if show_group(chat_id)["games"]:
            iddd = message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰رسائلك↫ ❲ {user_bot['msgs']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["رسائله"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if show_group(chat_id)["games"]:
            iddd = message.reply_to_message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰رسائله↫ ❲ {user_bot['msgs']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["سحكاتي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if show_group(chat_id)["games"]:
            iddd = message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰سحكاتك↫ ❲ {user_bot['shgs']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        msg_text in ["سحكاته"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if show_group(chat_id)["games"]:
            iddd = message.reply_to_message.from_user
            user_bot = show_user_info(chat_id, iddd.id)

            points = f"≭︰سحكاته↫ ❲ {user_bot['shgs']} ❳"
            bot.send_message(
                chat_id,
                f"<b> {points}</b>",
                reply_to_message_id=message.id,
                reply_markup=Bottom_channel_link(),
                parse_mode="HTML",
            )
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

    if (
        len(message.text.split(" ")) > 1
        and message.text.split(" ")[0] == "كول"
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if show_group(chat_id)["games"]:
            say = " ".join(message.text.split(" ")[1:])
            bot.send_message(
                chat_id,
                f"<b> {say}</b>",
                reply_to_message_id=message.id,
                parse_mode="HTML",
            )
            bot.delete_message(message.chat.id, message.id)
        else:
            bot.reply_to(message, "الالعاب معطله من قبل المنشئين")

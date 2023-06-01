import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling


def Ckick_Mute_Ban(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        msg_text in ["طرد"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = ban_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            bot.ban_chat_member(chat_id, IDD.id)
            Vandals.add_user(chat_id, IDD.id, is_banned=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["كتم"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = mute_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_muted=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["حظر"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = block_function_van(message, My_id)
        if "True" in FD2V:
            bot.get_chat_member(chat_id, IDD.id)
            bot.restrict_chat_member(
                chat_id,
                IDD.id,
                until_date=None,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
            )

            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_blocked=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["الغاء الكتم"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = unmute_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_muted=False)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["الغاء الحظر"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = unblock_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_blocked=False)
            bot.restrict_chat_member(
                chat_id,
                IDD.id,
                until_date=None,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            )
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["مسح المكتومين"]
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
            bot.send_message(
                chat_id, "تم مسح جميع المكتومين", reply_to_message_id=message.id
            )
            Vandals.delete_users(chat_id, is_muted=True)

        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["مسح المحظورين"]
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
            bot.send_message(
                chat_id, "تم مسح جميع المحظورين", reply_to_message_id=message.id
            )
            uss = Vandals.delete_users(chat_id, is_blocked=True)
            for user_id in uss:
                try:
                    bot.restrict_chat_member(
                        chat_id,
                        user_id,
                        until_date=None,
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_add_web_page_previews=True,
                    )
                except:
                    pass
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )
    if (
        msg_text in ["مسح المطرودين"]
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
            bot.send_message(
                chat_id, "تم مسح جميع المطرودين", reply_to_message_id=message.id
            )
            uss = Vandals.delete_users(chat_id, is_blocked=True)
            for user_id in uss:
                try:
                    bot.unban_chat_member(chat_id, user_id, only_if_banned=True)
                except:
                    pass
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

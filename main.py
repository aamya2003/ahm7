import telebot, time, datetime, random
from telebot.types import *
from database_main import *
from telebot.handler_backends import ContinueHandling
import random, os, config
from repl_0 import *
from performance_bot_private import *
from Local_replies import *
from Public_response_channel import *
from cmdGbot import *
from gamesBot import *

bot = telebot.TeleBot(config.Token)
insert_devloper_id()
insert_bot_name()
from functions_to_my_bots import *

from Lock_and_unlock_commands import *

from Upload_and_download_commands import *

from Identification_id import *

from Bot_join_commands import *


@bot.message_handler(chat_types=["supergroup"])
def Singin_use1r(message: Message):
    Sigin_user(message)
    update_user(message.chat.id, message.from_user.id, msgs=1)
    return ContinueHandling()


@bot.message_handler(
    chat_types=["supergroup"],
    content_types=[
        "photo",
        "sticker",
        "document",
        "video",
        "video_note",
        "voice",
        "audio",
        "animation",
    ],
)
def sendMedia_gr(message: Message):
    if check_group(message.chat.id):
        Is_not_member(message)
    return ContinueHandling()


@bot.message_handler(chat_types=["supergroup"])
def VBN(message: Message):
    Replies_s1(message)
    return ContinueHandling()


from Cick_Mute_Block import *


@bot.message_handler(content_types=["text"], chat_types=["supergroup"])
def Disable_and_activate(message: Message):
    if check_group(message.chat.id):
        SendTxtLo(message)
    cmdText(message)
    gamesBgr(message)
    Lock_Unlock(message)
    Upload_and_download(message)
    Identification_(message)
    Ckick_Mute_Ban(message)
    LOCALREOLIES(message)
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if msg_text == "تفعيل":
        chID = message.chat.id
        ADMIN = message.from_user

        info = bot.get_chat_member(message.chat.id, ADMIN.id)

        # is admin or crator or dev or not
        if info.status == "creator" or ADMIN.id == IsDevloper():
            # is group in database or not
            if not check_group(message.chat.id):
                # is bot has all premations or not
                if all_pre(bot, message.chat.id):
                    usnm = f'<a href="tg://user?id={ADMIN.id}">{ADMIN.first_name}</a>'
                    bot.send_message(
                        chat_id=chID,
                        text=f"تم تفعيل البوت في المجموعه \n تم التفعيل بواسطه: {usnm}",
                        parse_mode="HTML",
                        reply_to_message_id=message.id,
                    )
                    link = bot.create_chat_invite_link(
                        message.chat.id,
                        "link",
                    ).invite_link
                    grnm = f'<a href="{link}">{message.chat.title}</a>'
                    usnm = f'<a href="tg://user?id={ADMIN.id}">{ADMIN.first_name}</a>'
                    bot.send_message(
                        chat_id=IsDevloper(),
                        text=f" تم تفعيل البوت في {grnm} \n  تم تفعيل بواسطه: {usnm}",
                        parse_mode="HTML",
                        disable_web_page_preview=True,
                    )
                    insert_group(message.chat.id)
                    Automatic_lift(message.chat.id)

                else:
                    bot.send_message(
                        chat_id=message.chat.id,
                        text="عذرا, يجب اعطائي كافه الصلاحيات !",
                        parse_mode="HTML",
                    )
            else:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=f"⌔︙ تم تفعيلها مسبقا",
                    parse_mode="HTML",
                )
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text="هذا الامر مخصص للمالك و المطور  فقط",
                parse_mode="HTML",
            )

    if msg_text == "تعطيل":
        chID = message.chat.id
        ADMIN = message.from_user

        info = bot.get_chat_member(message.chat.id, ADMIN.id)

        # is admin or crator or dev or not
        if info.status == "creator" or ADMIN.id == IsDevloper():
            # is group in database or not
            if check_group(message.chat.id):
                # is bot has all premations or not
                if all_pre(bot, message.chat.id):
                    bot.send_message(
                        chat_id=chID,
                        text=f"-- تم تعطيل البوت في المجموعه \n -- تم التعطيل بواسطه: {ADMIN.first_name}",
                        parse_mode="HTML",
                    )
                    delete_group(message.chat.id)
                    bot.send_message(
                        chat_id=IsDevloper(),
                        text=f"تم تعطيل بوتك في مجموعه: {message.chat.title}",
                        parse_mode="HTML",
                    )

                else:
                    bot.send_message(
                        chat_id=message.chat.id,
                        text="عذرا, يجب اعطائي كافه الصلاحيات !",
                        parse_mode="HTML",
                    )
            else:
                bot.send_message(
                    chat_id=message.chat.id,
                    text=f"⌔︙ تم تعطيلها مسبقا",
                    parse_mode="HTML",
                )
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text="هذا الامر مخصص للمالك و المطور  فقط",
                parse_mode="HTML",
            )

    return ContinueHandling()


@bot.my_chat_member_handler()
def start_executor(message: ChatMemberUpdated):
    Bot_join(message)


@bot.channel_post_handler(content_types=["text"])
def ExistsState(message: Message):
    if IsChanell_reply_golbal() != "None":
        Control_public_response_channel(message)


@bot.message_handler(chat_types=["private"], content_types=["text"])
def b1(message: types.Message):
    send_member_private(message)


# @bot.chat_member_handler()
# def ChatMember1(message: ChatMemberUpdated):
#     chat_id = message.chat.id
#     user = message.from_user
#     n_us = message.new_chat_member
#     o_us = message.old_chat_member
#     if (
#         check_group(message.chat.id)
#         and show_group(message.chat.id)["AddDirect"] == True
#         and show_group(message.chat.id)["AddDirect"] == True
#         and IsDevloper() != message.from_user.id
#     ):
#         bot.delete_message(message.chat.id, message.id)


@bot.callback_query_handler(func=lambda call: True)
def callBackQuery(call: CallbackQuery):
    CallBack_query(call)
    cmdQuery(call)
    # C_1c(call)


@bot.edited_message_handler()
def On_edit(message: telebot.types.Message):
    update_user(message.chat.id, message.from_user.id, shgs=1)
    if (
        message.text
        and check_group(message.chat.id)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["EditMessage"] == False
        and IsDevloper() != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)


bot.infinity_polling(skip_pending=True, allowed_updates=telebot.util.update_types)

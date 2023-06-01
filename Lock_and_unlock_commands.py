import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling
from Ranks import *


def Is_not_member(message: Message):
    if Member_user(message.chat.id, message.from_user.id) and check_group(
        message.chat.id
    ):
        if message.photo and show_group(message.chat.id)["SendPhoto"] == False:
            bot.delete_message(message.chat.id, message.id)

        if (message.video or message.video_note) and show_group(message.chat.id)[
            "SendVideo"
        ] == False:
            bot.delete_message(message.chat.id, message.id)

        if message.voice and show_group(message.chat.id)["SendVoice"] == False:
            bot.delete_message(message.chat.id, message.id)

        if message.document and show_group(message.chat.id)["SendFiles"] == False:
            bot.delete_message(message.chat.id, message.id)

        if message.sticker and show_group(message.chat.id)["SendSticer"] == False:
            bot.delete_message(message.chat.id, message.id)

        if message.animation and show_group(message.chat.id)["SendAnmation"] == False:
            bot.delete_message(message.chat.id, message.id)

        return ContinueHandling()


def SendTxtLo(message: Message):
    det = Vandals.display_user_details(message.chat.id, message.from_user.id)
    if det is not None and det["is_muted"] == True:
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["sendMessage"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and Persian(message.text)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["SendParsionWord"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and English_words(message.text)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["SendEnglishWord"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and Links_word(message.text)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["SendLinks"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and Tag_per(message.text)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["Tag"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.text
        and check_group(message.chat.id)
        and Sharihaa(message.text)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["SendShariha"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.forward_from
        and check_group(message.chat.id)
        and Get_rank_user(message.chat.id, message.from_user.id) == "member"
        and show_group(message.chat.id)["SendFowrod"] == False
        and My_id != message.from_user.id
    ):
        bot.delete_message(message.chat.id, message.id)

    if (
        message.from_user.username == "Channel_Bot"
        and check_group(message.chat.id)
        and show_group(message.chat.id)["SendChannel"] == False
    ):
        bot.delete_message(message.chat.id, message.id)


def Lock_Unlock(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        msg_text in ["قفل الصور"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الصور", reply_to_message_id=message.id)
            update_group(chat_id, SendPhoto=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الصور"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الصور", reply_to_message_id=message.id)
            update_group(chat_id, SendPhoto=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الدردشه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الدردشه", reply_to_message_id=message.id)
            update_group(chat_id, sendMessage=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الدردشه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الدردشه", reply_to_message_id=message.id)
            update_group(chat_id, sendMessage=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الفيديو"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الفيديو", reply_to_message_id=message.id)
            update_group(chat_id, SendVideo=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الفيديو"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الفيديو", reply_to_message_id=message.id)
            update_group(chat_id, SendVideo=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الصوت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الصوت", reply_to_message_id=message.id)
            update_group(chat_id, SendVoice=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الصوت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الصوت", reply_to_message_id=message.id)
            update_group(chat_id, SendVoice=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الملصقات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الملصقات", reply_to_message_id=message.id)
            update_group(chat_id, SendSticer=False)

        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الملصقات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الملصقات", reply_to_message_id=message.id)
            update_group(chat_id, SendSticer=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل المتحركه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل المتحركه", reply_to_message_id=message.id)
            update_group(chat_id, SendAnmation=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح المتحركه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح المتحركه", reply_to_message_id=message.id)
            update_group(chat_id, SendAnmation=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الايموجي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الايموجي", reply_to_message_id=message.id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الايموجي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الايموجي", reply_to_message_id=message.id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الدخول"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الدخول", reply_to_message_id=message.id)
            update_group(chat_id, JoinMember=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الدخول"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الدخول", reply_to_message_id=message.id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الجهات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الجهات", reply_to_message_id=message.id)
            update_group(chat_id, AddDirect=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الجهات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الجهات", reply_to_message_id=message.id)
            update_group(chat_id, AddDirect=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الانجليزيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم قفل الانحليزي", reply_to_message_id=message.id
            )
            update_group(chat_id, SendEnglishWord=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الانجليزيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم فتح الانحليزي", reply_to_message_id=message.id
            )
            update_group(chat_id, SendEnglishWord=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الفارسيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الفارسيه", reply_to_message_id=message.id)
            update_group(chat_id, SendParsionWord=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الفارسيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الفارسيه", reply_to_message_id=message.id)
            update_group(chat_id, SendParsionWord=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الملفات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الملفات", reply_to_message_id=message.id)
            update_group(chat_id, SendFiles=False)

        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الملفات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الملفات", reply_to_message_id=message.id)
            update_group(chat_id, SendFiles=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل التثبيت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل التثبيت", reply_to_message_id=message.id)
            update_group(chat_id, Pin=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح التثبيت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح التثبيت", reply_to_message_id=message.id)
            update_group(chat_id, Pin=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل القناه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل القناه", reply_to_message_id=message.id)
            update_group(chat_id, SendChannel=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح القناه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح القناه", reply_to_message_id=message.id)
            update_group(chat_id, SendChannel=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الشارحه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الشارحه", reply_to_message_id=message.id)
            update_group(chat_id, SendShariha=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الشارحه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الشارحه", reply_to_message_id=message.id)
            update_group(chat_id, SendShariha=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل التكرار"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل التكرار", reply_to_message_id=message.id)
            update_group(chat_id, Looping=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح التكرار"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح التكرار", reply_to_message_id=message.id)
            update_group(chat_id, Looping=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الروابط"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الروابط", reply_to_message_id=message.id)
            update_group(chat_id, SendLinks=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الروابط"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الروابط", reply_to_message_id=message.id)
            update_group(chat_id, SendLinks=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الفشار"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الفشار", reply_to_message_id=message.id)
            update_group(chat_id, Sab=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الفشار"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الفشار", reply_to_message_id=message.id)
            update_group(chat_id, Sab=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل المعرفات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل المعرفات", reply_to_message_id=message.id)
            update_group(chat_id, SendTag=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح المعرفات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح المعرفات", reply_to_message_id=message.id)
            update_group(chat_id, SendTag=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل التاك"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل التاك", reply_to_message_id=message.id)
            update_group(chat_id, SendTag=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح التاك"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح التاك", reply_to_message_id=message.id)
            update_group(chat_id, SendTag=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل التوجيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل التوجيه", reply_to_message_id=message.id)
            update_group(chat_id, SendFowrod=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح التوجيه"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح التوجيه", reply_to_message_id=message.id)
            update_group(chat_id, SendFowrod=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل البوتات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل البوتات", reply_to_message_id=message.id)
            update_group(chat_id, AddBots=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح البوتات"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح البوتات", reply_to_message_id=message.id)
            update_group(chat_id, AddBots=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل التعديل"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل التعديل", reply_to_message_id=message.id)
            update_group(chat_id, EditMessage=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح التعديل"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح التعديل", reply_to_message_id=message.id)
            update_group(chat_id, EditMessage=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تفعيل الايدي بالصوره", "تفع"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم تفعيل الايدي بالصوره", reply_to_message_id=message.id
            )
            update_group(chat_id, show_PId=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تعطيل الايدي بالصوره", "تعط"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم تعطيل الايدي بالصوره", reply_to_message_id=message.id
            )
            update_group(chat_id, show_PId=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تعطيل الايدي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم تعطيل الايدي", reply_to_message_id=message.id)
            update_group(chat_id, show_id=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تفعيل الايدي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم تفعيل الايدي", reply_to_message_id=message.id)
            update_group(chat_id, show_id=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تعطيل الكشف"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم تعطيل الكشف", reply_to_message_id=message.id)
            update_group(chat_id, det_member=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تفعيل الكشف"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم تفعيل الكشف", reply_to_message_id=message.id)
            update_group(chat_id, det_member=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )
    if (
        msg_text in ["تعطيل الالعاب"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم تعطيل الالعاب", reply_to_message_id=message.id
            )
            update_group(chat_id, games=False)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تفعيل الالعاب"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(
                chat_id, "تم تفعيل الالعاب", reply_to_message_id=message.id
            )
            update_group(chat_id, games=True)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["قفل الكل"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم قفل الكل", reply_to_message_id=message.id)
            LockAll_Group(chat_id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["فتح الكل"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "admin",
            "blocked",
            "muted",
            "banned",
            "reeve",
        ]:
            bot.send_message(chat_id, "تم فتح الكل", reply_to_message_id=message.id)
            UnLockAll_Group(chat_id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمنشئين فقط", reply_to_message_id=message.id
            )

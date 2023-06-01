import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling

user_rep_id, Adrp_id = None, None


def Replies_s1(message: Message):
    global user_rep_id, Adrp_id, msg
    msg = message
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    user_rep_id = user_.id

    if (
        msg_text in ["اضف رد"]
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
            ttxt = "✯︙ ارسل الان الكلمه لاضافتها في الردود"
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=". الغاء الامر .", callback_data="del_mrk")
            mrk.add(btn)
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=mrk
            )
            bot.register_next_step_handler(message, Replies_s2)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["اضف توحيد"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
            "reeve",
        ]:
            ttxt = "✯︙ ارسل الان التوحيد"
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=". الغاء الامر .", callback_data="del_mrk")
            mrk.add(btn)
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=mrk
            )
            bot.register_next_step_handler(message, AddTowheadGr)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص  للمنشئين فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["اضف لقب"]
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
            if message.reply_to_message:
                Adrp_id = message.reply_to_message.from_user.id

            ttxt = "✯︙ ارسل الان اللقب"
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=". الغاء الامر .", callback_data="del_mrk")
            mrk.add(btn)
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=mrk
            )
            bot.register_next_step_handler(message, SetNickName)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        len(message.text.split(" ")) == 3
        and message.text.startswith("اضف نقاط")
        and message.text.split(" ")[2].isnumeric()
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
        and message.reply_to_message.from_user.id != bot.get_me().id
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم اضافه له ( {message.text.split(" ")[2]} ) من النقاط
✓"""
            bot.send_message(
                chat_id,
                ttxt,
                reply_to_message_id=message.id,
            )
            update_user(
                chat_id,
                message.reply_to_message.from_user.id,
                points=int(message.text.split(" ")[2]),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        len(message.text.split(" ")) == 3
        and message.text.startswith("اضف سحكات")
        and message.text.split(" ")[2].isnumeric()
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
        and message.reply_to_message.from_user.id != bot.get_me().id
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم اضافه له ( {message.text.split(" ")[2]} ) من السحكات
✓"""
            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            update_user(
                chat_id,
                message.reply_to_message.from_user.id,
                shgs=int(message.text.split(" ")[2]),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        len(message.text.split(" ")) == 3
        and message.text.startswith("اضف رسائل")
        and message.text.split(" ")[2].isnumeric()
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
        and message.reply_to_message.from_user.id != bot.get_me().id
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم اضافه له ( {message.text.split(" ")[2]} ) من الرسائل
✓"""
            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            update_user(
                chat_id,
                message.reply_to_message.from_user.id,
                msgs=int(message.text.split(" ")[2]),
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        message.text in ["مسح رسائلي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم مسح رسائلك
✓"""
            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            deleteUserProperty(
                chat_id,
                message.from_user.id,
                msgs=True,
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        message.text in ["مسح نقاطي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم مسح نقاطك
✓"""
            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            deleteUserProperty(
                chat_id,
                message.from_user.id,
                points=True,
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        message.text in ["مسح سحكاتي"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            ttxt = f"""
✯︙ تم مسح سحكاتك
✓"""
            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            deleteUserProperty(
                chat_id,
                message.from_user.id,
                shgs=True,
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["مسح رد"]
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
            ttxt = "✯︙ ارسل الان الرد لمسحه من المجموعة"
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=". الغاء الامر .", callback_data="del_mrk")
            mrk.add(btn)
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=mrk
            )
            bot.register_next_step_handler(message, DEL_Replies_s2)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["مسح الردود"]
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
            ttxt = "✯︙ تم مسح جميع الردود من المجموعة"

            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
            for fi in show_all_reps_grps(message.chat.id).values():
                try:
                    os.remove(fi["reply"])
                except:
                    pass
            Delete_reps_by_chat_id(message.chat.id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["تغيير اسم البوت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if user_.id == My_id:
            ttxt = "✯︙ ارسل الان اسم  البوت الجديد"
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(text=". الغاء الامر .", callback_data="del_mrk")
            mrk.add(btn)
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=mrk
            )
            bot.register_next_step_handler(message, Set_bot_name)
        else:
            bot.send_message(
                chat_id,
                "هذا الامر مخصص للمطور الاساسي فقط",
                reply_to_message_id=message.id,
            )


def Replies_s2(message: Message):
    global msg_s1_rep_name
    if message.from_user.id == user_rep_id and message.text:
        msg_s1_rep_name = message.text
        ttxt = """ارسل لي الرد سواء أكان
❨ ملف ✯︙ ملصق ✯︙ متحركه ✯︙ صوره
 ✯︙ فيديو ✯︙ بصمه الفيديو ✯︙ بصمه ✯︙ صوت ✯︙ رساله ❩
  يمكنك اضافة الى النص ✯︙
━━━━━━━━━━━
 #username ↬ معرف المستخدم
 #name ↬ اسم المستخدم
 #id ↬ ايدي المستخدم
"""
        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        bot.register_next_step_handler(message, Replies_s3)
    else:
        bot.register_next_step_handler(message, Replies_s2)
    return ContinueHandling()


def AddTowheadGr(message: Message):
    global msg_s1_rep_name
    if message.from_user.id == user_rep_id and message.text:
        msg_s1_rep_name = message.text
        ttxt = "✯︙ تم حفظ التوحيد"

        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        update_group(message.chat.id, towheed=message.text)

    else:
        bot.register_next_step_handler(message, AddTowheadGr)
    return ContinueHandling()


def SetNickName(message: Message):
    global msg_s1_rep_name
    if message.from_user.id == user_rep_id and message.text:
        msg_s1_rep_name = message.text
        ttxt = "✯︙ تم حفظ اللقب"
        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        if type(Adrp_id) == None:
            update_user(message.chat.id, message.from_user.id, nickname=message.text)
        else:
            update_user(message.chat.id, Adrp_id, nickname=message.text)
    else:
        bot.register_next_step_handler(message, SetNickName)
    return ContinueHandling()


def Replies_s3(message: Message):
    if message.from_user.id == user_rep_id:
        ttxt = "✯︙ تم حفظ الرد"
        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        save_replies_into_db(msg_s1_rep_name, message)

    else:
        bot.register_next_step_handler(message, Replies_s3)


def DEL_Replies_s2(message: Message):
    global msg_s1_rep_name
    if message.from_user.id == user_rep_id and message.text:
        msg_s1_rep_name = message.text
        ttxt = "تم مسح الرد من المجموعة"
        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        delete_rep(message.chat.id, message.text)
    else:
        bot.register_next_step_handler(message, DEL_Replies_s2)


def Set_bot_name(message: Message):
    if message.from_user.id == user_rep_id and message.text:
        msg_s1_rep_name = message.text
        ttxt = "تم تعيين اسم البوت الجديد."
        bot.send_message(message.chat.id, ttxt, reply_to_message_id=message.id)
        update_bot_name(message.text)
    else:
        bot.register_next_step_handler(message, Set_bot_name)


def C_1c(call: CallbackQuery):
    if call.data == "del_mrk" and call.from_user.id == user_rep_id:
        bot.clear_reply_handlers(msg)
        bot.edit_message_text(
            "تم الغاء الامر",
            call.message.chat.id,
            call.message.id,
            reply_markup=Bottom_channel_link(),
        )

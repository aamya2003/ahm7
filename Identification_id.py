import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling
import random


def Identification_(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        msg_text == "رتبته"
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            rankbt = ""
            if IsDevloper() == iddd.id:
                rankbt = "مطور اساسي"
            else:
                rankbt = convertRank2Ar(Get_rank(chat_id, iddd.id))
            rankgr = (
                "عضو" if bot.get_chat_member(chat_id, iddd.id).is_member else "مشرف"
            )
            rankbt = convertRank2Ar(Get_rank(chat_id, iddd.id))

            xt = f"""﹃
≭︰رتبته في البوت ↫ ❲ {rankbt} ❳ 
≭︰رتبته في الگروب ↫ ❲ {rankgr} ❳
﹄"""
            bot.send_message(chat_id, xt, reply_to_message_id=message.id)

        else:
            pass
    if (
        msg_text == "لقبه"
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        iddd = message.reply_to_message.from_user

        if not (bot.get_me().id == iddd.id or user_.id == iddd.id):
            stategr = ""
            statebt = Get_nickname_user(chat_id, iddd.id)

            status = bot.get_chat_member(chat_id, iddd.id)
            if not status.is_member:
                if status.custom_title:
                    stategr = status.custom_title
                else:
                    stategr = "غير معروف"

            xt = f"""﹃
≭︰لقبه في البوت ↫ ❲ {statebt} ❳ 
≭︰لقبه في الگروب ↫ ❲ {stategr} ❳
﹄
"""

            bot.send_message(chat_id, xt, reply_to_message_id=message.id)

        else:
            pass
    if (
        msg_text == "كشف"
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        if show_group(chat_id)["det_member"] == True:
            iddd = message.reply_to_message.from_user
            name = iddd.first_name if iddd.first_name else iddd.last_name
            username = "@" + iddd.username if iddd.username else "غير معروف"
            user_bot = show_user_info(chat_id, iddd.id)
            rank_bot = convertRank2Ar(Get_rank_user(chat_id, iddd.id))
            msgs = user_bot["msgs"]
            points = user_bot["points"]
            edit = user_bot["shgs"]
            restrictions = "لا شيئ"
            directions = user_bot["directs"]
            nickname = Get_nickname_user(chat_id, iddd.id)
            rank_group = ""
            status = bot.get_chat_member(chat_id, iddd.id).status
            if status == "member":
                rank_group = "عضو"
            elif status == "creator":
                rank_group = "مالك"
            elif "admin" in status:
                rank_group = "مشرف"

            if not (bot.get_me().id == iddd.id):
                nm = """
    ≭︰اسمه ↫ ❲ {name} ❳
    ≭︰ايديه ↫❲ {user_id} ❳
    ≭︰معرفه ↫ ❲ {username} ❳
    ≭︰رتبه البوت ↫ ❲ {rank_bot} ❳
    ≭︰رتبه الكروب ↫ ❲ {rank_group} ❳
    ≭︰رسائله ↫ ❲ {msgs} ❳
    ≭︰نقاطه ↫ ❲ {points} ❳
    ≭︰تعديلاته ↫ ❲ {edit} ❳
    ≭︰جهاته ↫ ❲ {directions} ❳
    ≭︰قيوده ↫ ❲ {restrictions} ❳
    ≭︰لقبه ↫ ❲ {nickname}❳
    `
                """.format(
                    name=name,
                    user_id=iddd.id,
                    username=username,
                    rank_bot=rank_bot,
                    rank_group=rank_group,
                    msgs=msgs,
                    points=points,
                    directions=directions,
                    restrictions=restrictions,
                    nickname=nickname,
                    edit=edit,
                )

                bot.send_message(chat_id, nm, reply_to_message_id=message.id)

            else:
                pass
        else:
            bot.send_message(
                chat_id,
                "الكشف معطل من قبل المنشئين",
                reply_to_message_id=message.id,
            )
    if (
        msg_text == "رتبتي"
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        iddd = user_
        rankbt = convertRank2Ar(Get_rank(chat_id, iddd.id))
        rankgr = "عضو" if bot.get_chat_member(chat_id, user_.id).is_member else "مشرف"

        xt = f"""﹃
≭︰رتبتك في البوت ↫ ❲ {rankbt} ❳ 
≭︰رتبتك في الگروب ↫ ❲ {rankgr} ❳
        ﹄"""
        bot.send_message(chat_id, xt, reply_to_message_id=message.id)

    if msg_text == "لقبي" and Compulsory_subscription(message) and check_group(chat_id):
        stategr = ""
        statebt = Get_nickname_user(chat_id, user_.id)

        status = bot.get_chat_member(chat_id, user_.id)
        if not status.is_member:
            if status.custom_title:
                stategr = status.custom_title
            else:
                stategr = "غير معروف"

        xt = f"""                       ﹃
    
≭︰لقبك في البوت ↫ ❲ {statebt} ❳ 
≭︰لقبك في الگروب ↫ ❲ {stategr} ❳
﹄
"""

        bot.send_message(chat_id, xt, reply_to_message_id=message.id)

    if (
        msg_text in ["المطور", "مطور"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        cid = IsDevloper() if Ischannell() == "None" else Ischannell()

        chan_inf = bot.get_chat(cid)

        def Mrk():
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(
                text=chan_inf.title if chan_inf.title else chan_inf.first_name,
                url="https://t.me/" + chan_inf.username,
            )
            mrk.add(btn)
            return mrk

        bio = bot.get_chat(My_id)
        Photo_user = f"https://t.me/{bio.username}"
        ttxt = f"""✯︙𝙽𝙰𝙼𝙴 : {bio.first_name}
✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{bio.username}
✯︙𝙸𝙳 : {bio.id} .
✯︙𝙱𝙸𝙾 :  {bio.bio}) ."""
        try:
            bot.send_photo(
                chat_id,
                Photo_user,
                reply_to_message_id=message.id,
                caption=ttxt,
                reply_markup=Mrk(),
            )
        except:
            bot.send_message(
                chat_id,
                ttxt,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=bio.first_name, id=bio.id),
            )

    if (
        msg_text in ["المالك", "مالك"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        allAdminsss = bot.get_chat_administrators(chat_id)
        Admins = [Admin.user for Admin in allAdminsss if Admin.status == "creator"]
        for user in Admins:
            user_inf = bot.get_chat(user.id)

            Photo_user = f"https://t.me/{user_inf.username}"
            ttxtx = f"""- معلومات المالك : 
✯︙name: ⤿ {user_inf.first_name}

✯︙user : ⤿  @{user_inf.username}

✯︙Bio: ⤿ #{user_inf.bio}"""

        try:
            bot.send_photo(
                chat_id,
                Photo_user,
                caption=ttxtx,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=user_inf.first_name, id=user_inf.id),
            )

        except:
            bot.send_message(
                chat_id,
                ttxtx,
                reply_to_message_id=message.id,
                reply_markup=Get_prerson(name=user_inf.first_name, id=user_inf.id),
            )

    if (
        msg_text in ["السورس", "سورس"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        cid = IsDevloper() if Ischannell() == "None" else Ischannell()

        chan_inf = bot.get_chat(cid)

        def Mrk():
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(
                text=chan_inf.title if chan_inf.title else chan_inf.first_name,
                url="https://t.me/" + chan_inf.username,
            )
            mrk.add(btn)
            return mrk

        Photo_user = f"https://t.me/{chan_inf.username}"
        ttttxt = f"""𝑆𝑂𝑈𝑅𝐶𝐸 {chan_inf.title if chan_inf.title else chan_inf.first_name} ❍ 

˹ 𝙻𝙴𝙰𝙳𝙴𝚁 AHMAD ASAAD
~"""
        try:
            bot.send_photo(
                chat_id,
                Photo_user,
                caption=ttttxt,
                reply_to_message_id=message.id,
                reply_markup=Mrk(),
            )

        except:
            bot.send_photo(
                chat_id, ttttxt, reply_to_message_id=message.id, reply_markup=Mrk()
            )

    if (
        msg_text in ["مطور السورس", "مطور سورس"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        chan_inf = bot.get_chat(Ischannell())

        def Mrk():
            mrk = InlineKeyboardMarkup()
            btn = InlineKeyboardButton(
                text=chan_inf.title if chan_inf.title else chan_inf.first_name,
                url="https://t.me/" + chan_inf.username,
            )
            mrk.add(btn)
            return mrk

        bio = bot.get_chat(My_id)
        Photo_user = f"https://t.me/{bio.username}"
        ttxt = f"""- ??𝒐𝒖𝒓𝒄𝒆 𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏:
✯︙𝙽𝙰𝙼𝙴 : {bio.first_name}.
✯︙𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{bio.username}
✯︙𝙸𝙳 : {bio.id} .
✯︙𝙱𝙸𝙾 :  {bio.bio}) ."""
        try:
            bot.send_photo(
                chat_id,
                Photo_user,
                caption=ttxt,
                reply_to_message_id=message.id,
                reply_markup=Mrk(),
            )
        except:
            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, reply_markup=Mrk()
            )

    if (
        message.text in ["id", "/id", "ايدي", "ا"]
        and check_group(chat_id)
        and Compulsory_subscription(message)
    ):
        user = message.from_user
        chat_id = message.chat.id
        # Check if reply message or normal message
        if message.reply_to_message:
            user = message.reply_to_message.from_user
        if show_group(chat_id)["show_id"] == True:
            Id_user = user.id
            UserName = "@" + user.username if user.username else "لا يوجد"

            First_name = user.first_name if user.first_name else ""
            Last_name = user.last_name if user.last_name else ""
            Full_name = First_name + " " + Last_name

            Photo_user = f"https://t.me/{user.username}"

            Rank_User = bot.get_chat_member(chat_id, user.id).status
            if Rank_User == "administrator":
                Rank_User = "مشرف"
            elif Rank_User == "member":
                Rank_User = "عضو"
            elif Rank_User == "creator":
                Rank_User = "مالك"

            Msgs = show_user_info(chat_id, user.id)["msgs"]
            Edited_msg = show_user_info(chat_id, user.id)["shgs"]
            Rndom_bio = random.choice(
                [
                    "- لا يمكن تحقيق النجاح إلا إذا أحببت ما تقوم به",
                    "باެنيـݪك بڪِݪبيہَ بيۅتِ بـَسہ طِاحَـטּ  .",
                    "كلما زاد الحديث قل التصديق .",
                ]
            )

            def IdetId(text):
                text = text.replace("#description", str(Rndom_bio))
                text = text.replace("#id", str(Id_user))
                text = text.replace("#username", UserName)
                text = text.replace("#name", Full_name)
                text = text.replace("#msgs", str(Msgs))
                text = text.replace("#shgs", str(Edited_msg))
                text = text.replace(
                    "#rank", str(convertRank2Ar(Get_rank_user(chat_id, user.id)))
                )
                return text

            txt = """#description

•❃  الاســم  › #name
•❃  الايـدي  › #id
•❃  المـعـرف › #username
•❃ الرسـائـل › #msgs
•❃ السحـگـات › #shgs
 •❃  الرتبـــه  ⇦ .「   #rank 𓅫  」. 
            """
            Full_clich = IdetId(txt)

            def mrk():
                mrk = telebot.types.InlineKeyboardMarkup()
                btn = telebot.types.InlineKeyboardButton(
                    text=Full_name, callback_data="Photo_user"
                )
                mrk.add(btn)
                return mrk

            if show_group(chat_id)["show_PId"]:
                try:
                    # If User not have photo
                    bot.send_photo(
                        chat_id,
                        Photo_user,
                        caption=Full_clich,
                        reply_markup=mrk(),
                        reply_to_message_id=message.id,
                    )
                except:
                    # If User have photo
                    bot.send_message(
                        chat_id,
                        Full_clich,
                        reply_markup=mrk(),
                        reply_to_message_id=message.id,
                    )
            else:
                bot.send_message(
                    chat_id,
                    Full_clich,
                    reply_markup=mrk(),
                    reply_to_message_id=message.id,
                )
        else:
            bot.send_message(
                chat_id,
                "الايدي معطل من قبل المنشئين",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["الردود", "رر"]
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
            repls = ShowAllRep_Group(message.chat.id)
            ttxt = "✯︙ هذه الردود  الخاصة بالمجموعة"
            a = 1
            for rep in repls.values():
                n = rep["name"]
                t = rep["type"]
                ttxt += f"✯ {a} ✯︙ ( {n} )  - ( {t} )"
                a += 1

            bot.send_message(chat_id, ttxt, reply_to_message_id=message.id)
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["ثبت", "تثبيت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if show_group(chat_id)["Pin"]:
            if Get_rank_user(chat_id, user_.id) not in [
                "member",
                "distinct",
                "blocked",
                "muted",
                "banned",
                "admin",
            ]:
                bot.pin_chat_message(chat_id, message.reply_to_message.id)
            else:
                bot.send_message(
                    chat_id,
                    "هذا الامر مخصص للمدراء فقط",
                    reply_to_message_id=message.id,
                )
        else:
            bot.reply_to(message, "التثبيت مقفل من قبل المنشئين")
    if (
        msg_text in ["ثبت", "تثبيت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if show_group(chat_id)["Pin"]:
            if Get_rank_user(chat_id, user_.id) not in [
                "member",
                "distinct",
                "blocked",
                "muted",
                "banned",
                "admin",
            ]:
                bot.pin_chat_message(chat_id, message.reply_to_message.id)
            else:
                bot.send_message(
                    chat_id,
                    "هذا الامر مخصص للمدراء فقط",
                    reply_to_message_id=message.id,
                )
        else:
            bot.reply_to(message, "التثبيت مقفل من قبل المنشئين")
    if (
        msg_text in ["مسح الرساله", "مسح"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            bot.delete_message(chat_id, message.reply_to_message.id)
            bot.delete_message(chat_id, message.id)
        else:
            bot.send_message(
                chat_id,
                "هذا الامر مخصص للمدراء فقط",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["الغاء تثبيت", "الغاء التثبيت"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
        and message.reply_to_message
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
            "admin",
        ]:
            bot.unpin_chat_message(chat_id, message.reply_to_message.id)
            bot.delete_message(chat_id, message.id)
        else:
            bot.send_message(
                chat_id,
                "هذا الامر مخصص للمدراء فقط",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["الغاء تثبيت الرسائل", "الغاء تثبيت كل الرسائل"]
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
            bot.reply_to(message, "تم الغاء تثبيت كل الرسائل")
            bot.unpin_all_chat_messages(chat_id)
        else:
            bot.send_message(
                chat_id,
                "هذا الامر مخصص للمدراء فقط",
                reply_to_message_id=message.id,
            )

    if (
        msg_text in ["توحيد", "توحيد المجموعه"]
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
            TW = (
                show_group(chat_id)["towheed"]
                if show_group(chat_id)["towheed"]
                else "ماكو"
            )
            TW = f"<pre> {TW} </pre>"
            ttxt = f"✯︙ االتوحيد: انقر لنسخة: {TW}"

            bot.send_message(
                chat_id, ttxt, reply_to_message_id=message.id, parse_mode="HTML"
            )
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للادمينه فقط", reply_to_message_id=message.id
            )

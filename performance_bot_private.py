from telebot import *
from telebot.types import *
from time import sleep, time
from database_main import *

# from keepAlive import keep_alive


import telebot, time
from time import time
from telebot import types
from functions_to_my_bots import *
import messagesBots

# My_id = IsDevloper()


def Decor(text, type=[None, "b", "s", "del", "pre", "user", "url"], id=None, url=None):
    if type != None:
        if type == "b":
            return f"<b>{text}</b>"

        elif type == "s":
            return f"<s>{text}</s>"

        elif type == "del":
            return f"<del>{text}</del>"

        elif type == "pre":
            return f"<code>{text}</code>"

        elif type == "user":
            return f"""<a href='tg://user?id={id}'>  {text}  </a>"""

        elif type == "url":
            return f"<a href={url}>{text}</a>"


def must_sub(bot, msg, Group_ID, InlineKeyboardMarkup, InlineKeyboardButton):
    # Create an invite link class that contains info about the created invite link using create_chat_invite_link() with parameters
    invite = bot.create_chat_invite_link(
        Group_ID, member_limit=1, expire_date=int(time()) + 45
    )  # Here, the link will auto-expire in 45 seconds
    InviteLink = invite.invite_link  # Get the actual invite link from 'invite' class

    mrkplink = InlineKeyboardMarkup()  # Created Inline Keyboard Markup
    mrkplink.add(
        InlineKeyboardButton(bot.get_chat(Group_ID).title, url=InviteLink)
    )  # Added Invite Link to Inline Keyboard

    m = bot.send_message(
        msg.chat.id, Ismessage(), reply_markup=mrkplink, reply_to_message_id=msg.id
    )
    return m


def mycommands_on():
    mrk = ReplyKeyboardMarkup(row_width=6)
    TONE = "⭕️" if bool(IsBool()) else "❌"

    btns = [
        KeyboardButton(text=f"اشعار الدخول {TONE} "),
        KeyboardButton(text="قسم الاشتراك الاجباري"),
        KeyboardButton(text="الاحصائيات"),
        KeyboardButton(text="رساله الترحيب"),
        KeyboardButton(text="الاذاعة"),
        KeyboardButton(text="الادمينة"),
        KeyboardButton(text="المحظورين"),
        KeyboardButton(text="الردود العامة"),
        KeyboardButton(text="اخفاء"),
    ]
    mrk.add(*btns)
    return mrk


def AdminsSitting():
    mrkup = ReplyKeyboardMarkup()
    btns = [
        KeyboardButton(text="عرض الادمينة"),
        KeyboardButton(text="تغيير المطور"),
        KeyboardButton(text="اضف ادمن"),
        KeyboardButton(text="مسح ادمن"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrkup.add(*btns)
    return mrkup


def MutedSitting():
    mrkup = ReplyKeyboardMarkup(row_width=2)
    btns = [
        KeyboardButton(text="عرض المحظورين"),
        KeyboardButton(text="مسح محظور"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrkup.add(*btns)
    return mrkup


def slide_sub():
    mrk = ReplyKeyboardMarkup(row_width=2)
    btns = [
        KeyboardButton(text="تعيين قناه"),
        KeyboardButton(text="مسح قناه"),
        KeyboardButton(text="تعيين رساله الاشتراك الاجباري"),
        KeyboardButton(text="حذف رساله الاشتراك الاجباري"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrk.add(*btns)
    return mrk


def Public_responses():
    mrk = ReplyKeyboardMarkup(row_width=2)
    btns = [
        KeyboardButton(text="اضف رد"),
        KeyboardButton(text="مسح رد"),
        KeyboardButton(text="عرض رد"),
        KeyboardButton(text="قناه للردود العامه"),
        KeyboardButton(text="مسح كل الردود"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrk.add(*btns)
    return mrk


def Chanell_Public_responses():
    mrk = ReplyKeyboardMarkup(row_width=2)
    btns = [
        KeyboardButton(text="اضف قناه ردود"),
        KeyboardButton(text="مسح قناه ردود"),
        KeyboardButton(text="عرض قناه ردود"),
        KeyboardButton(text="قسم قناه الردود"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrk.add(*btns)
    return mrk


def join_members(message: types.Message):
    global senderMsg
    if check_muted(message.from_user.id):
        senderMsg = [message.from_user, message.id]
        user = message.from_user
        full_name = str(user.first_name) + " " + str(user.last_name)
        username = str(user.username)
        Ids = int(user.id)
        msg = message.text
        name = Decor(full_name, id=Ids, type="user")
        if message.text != "/start":
            if showGloblaReply(message.text):
                bot.send_message(
                    message.chat.id,
                    Decor(showGloblaReply(message.text), "b"),
                    parse_mode="HTML",
                    reply_to_message_id=message.id,
                )

            bot.send_message(
                IsDevloper(),
                Decor(f" الرسالة; {msg}", "b"),
                parse_mode="HTML",
                reply_markup=reply_mrk(),
            )

            bot.send_message(IsDevloper(), Decor(f"من; {name}", "b"), parse_mode="HTML")
        else:
            gtme = bot.get_me()
            try:
                bot.send_photo(
                    message.chat.id,
                    photo="https://t.me/" + gtme.username,
                    caption=Decor(
                        Ismessage_join_member().format(
                            bot_name=gtme.first_name,
                            bot_username=gtme.username,
                            dev_username=bot.get_chat(IsDevloper()).username,
                        ),
                        "b",
                    ),
                    parse_mode="HTML",
                    reply_to_message_id=message.id,
                    reply_markup=Bottom_channel_link(),
                )
            except:
                bot.send_message(
                    message.chat.id,
                    text=Decor(
                        Ismessage_join_member().format(
                            bot_name=gtme.first_name,
                            bot_username=gtme.username,
                            dev_username=bot.get_chat(IsDevloper()).username,
                        ),
                        "b",
                    ),
                    parse_mode="HTML",
                    reply_to_message_id=message.id,
                    reply_markup=Bottom_channel_link(),
                )

        if check_user(Ids):
            if IsBool():
                print(True)
                user = message.from_user
                name = user.first_name
                name = name if user.first_name else "غير معروف"
                id = user.id
                username = user.username
                username = username if user.username else "غير معروف"

                text = f"""تم انظمام مسخدم جديد الى البوت \n الاسم: {name} \n الايدي: {id} \n المعرف: {username}"""
                bot.send_message(IsDevloper(), Decor(text, "b"), parse_mode="HTML")
                for i in IdsAdmins():
                    try:
                        bot.send_message(i, Decor(text, "b"), parse_mode="HTML")
                    except:
                        User_private.update_user_private(
                            IsDevloper(), i, is_admin=False
                        )
            User_private.add_user_private(IsDevloper(), Ids, is_member=True)
    else:
        bot.send_message(
            message.chat.id,
            Decor("انت محظور, لا يمكنك الارسال....", "b"),
            parse_mode="HTML",
            reply_to_message_id=message.id,
        )


# def SendPrivateStart(message: Message):
#     command = message.text
#     chat_id = message.chat.id
#     CHid = message.from_user.id


def Broadcast():
    keyboard = ReplyKeyboardMarkup(row_width=2)
    List_button = [
        KeyboardButton(text="اذاعه للاعضاء"),
        KeyboardButton(text="اذاعه للمجاميع"),
        KeyboardButton(text=". رجوع ."),
    ]
    keyboard.add(*List_button)
    return keyboard


def send_member_private(message: types.Message):
    global cv, vc
    mtxt = message.text
    CHid = message.from_user.id

    if CHid == IsDevloper() or CHid in IdsAdmins():
        if mtxt == "اشعار الدخول ⭕️":
            a = (
                "تم تعطيل اشعار الدخول"
                if not bool(IsBool())
                else "تم فتح اشعارت الدخول"
            )
            bot.send_message(
                message.chat.id,
                reply_markup=mycommands_on(),
                text=a,
            )
            update_commnds("False")

        if mtxt == "/start":
            bot.send_message(
                message.chat.id,
                text=messagesBots.message_for_admin,
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=mycommands_on(),
            )

        if mtxt == "اشعار الدخول ❌":
            a = (
                "تم تعطيل اشعار الدخول"
                if not bool(IsBool())
                else "تم فتح اشعارت الدخول"
            )
            bot.send_message(
                message.chat.id,
                reply_markup=mycommands_on(),
                text=a,
            )
            update_commnds("True")
        if mtxt == "الردود العامة":
            bot.send_message(
                message.chat.id,
                reply_markup=Public_responses(),
                text="اهلا بك في قسم الردود العامة!",
            )

        if mtxt == "قناه للردود العامه":
            bot.send_message(
                message.chat.id,
                reply_markup=Chanell_Public_responses(),
                text="حدد امر.",
            )

        if mtxt == "رجوع الى قسم للردود العامه":
            bot.send_message(
                message.chat.id,
                reply_markup=Chanell_Public_responses(),
                text="حدد امر.",
            )

        if mtxt == "اضف قناه ردود":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم للردود العامه"))

            bot.send_message(
                message.chat.id, reply_markup=mrk, text=sign_chanell_message
            )
            bot.register_next_step_handler(message, Add_chanell_global_replay)

        if mtxt == "عرض قناه ردود":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم للردود العامه"))

            if IsChanell_reply_golbal() != "None":
                ch = bot.get_chat(IsChanell_reply_golbal())
                nc = ch.title
                uc = "@" + str(ch.username)
                ic = ch.id
                tst = f"اسم القناه: {nc} \n معرف القناه: {uc} \n ايدي القناه: {ic}"
                bot.send_message(message.chat.id, reply_markup=mrk, text=tst)
            else:
                bot.send_message(
                    message.chat.id, reply_markup=mrk, text="ليس لديك قناه ردود!"
                )

        if mtxt == "مسح قناه ردود":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم للردود العامه"))

            bot.send_message(
                message.chat.id,
                reply_markup=mrk,
                text="تم حذف قناه الردود",
            )
            try:
                bot.leave_chat(IsChanell_reply_golbal())
            except:
                pass

            deleteChanell_reply_golbal()

        if mtxt == "قسم قناه الردود":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم للردود العامه"))

            bot.send_message(
                message.chat.id,
                reply_markup=mrk,
                text=InformationChannelreply,
            )

        if mtxt == "اضف رد":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text=". رجوع ."))

            bot.send_message(
                message.chat.id,
                reply_markup=mrk,
                text="ارسل اسم الرد الان",
            )
            bot.register_next_step_handler(message, Add_Public_responses)

        if mtxt == "مسح رد":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text=". رجوع ."))
            bot.send_message(
                message.chat.id,
                reply_markup=mrk,
                text="ارسل اسم الرد الان",
            )

            bot.register_next_step_handler(message, Del_Public_responses)

        if mtxt == "مسح كل الردود":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text=". رجوع ."))
            bot.send_message(message.chat.id, text="تم مسح كل الردود", reply_markup=mrk)
            DelAll_general_response_from_the_bot()
        if mtxt == "عرض رد":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text=". رجوع ."))
            bot.send_message(
                message.chat.id,
                reply_markup=mrk,
                text="ارسل اسم الرد الان",
            )
            bot.register_next_step_handler(message, Sho_Public_responses)

        if mtxt == "قسم الاشتراك الاجباري":
            a = (
                "لا يوجد"
                if Ischannell() == "None"
                else bot.get_chat(Ischannell()).title
            )
            bot.send_message(
                message.chat.id,
                reply_markup=slide_sub(),
                text=messagesBots.Compulsory_subscription_letter_dep.format(
                    a=a, b=Ismessage()
                ),
            )

        if mtxt == ". رجوع .":
            bot.clear_step_handler(message)
            bot.send_message(
                message.chat.id,
                reply_markup=mycommands_on(),
                text=messagesBots.message_for_admin,
            )

        if mtxt == "اخفاء":
            ReplyKeyboardRemove(mycommands_on())
        if mtxt == "الرجوع الى قسم الاشتراك الاجباري":
            bot.send_message(
                message.chat.id,
                reply_markup=slide_sub(),
                text=messagesBots.Compulsory_subscription_letter_dep.format(
                    a=Ischannell(), b=Ismessage()
                ),
            )
        if mtxt == "تعيين قناه":
            bot.send_message(
                text=messagesBots.sign_chanell_message,
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, sign_chanell)
        if mtxt == "مسح قناه":
            bot.send_message(
                text="- تم حذف القناه 💞",
                chat_id=message.chat.id,
                reply_markup=slide_sub(),
            )
            deleteChanell()
        if mtxt == "تعيين رساله الاشتراك الاجباري":
            bot.send_message(
                text="ارسل كليشه الاشتراك الان: ",
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, sign_message)

        if mtxt == "حذف رساله الاشتراك الاجباري":
            bot.send_message(
                text="- تم حذف رساله الاشتراك الاجباري 💞",
                chat_id=message.chat.id,
                reply_markup=slide_sub(),
            )
            update_message("⌔︙عليك الاشتراك في قناة البوت لأستخدام الاوامر🚀.")

        if mtxt == "رساله الترحيب":
            gtme = bot.get_me()
            bot.send_message(
                text=messagesBots.Welcome_message.format(
                    msg=Ismessage_join_member().format(
                        bot_name=gtme.first_name,
                        bot_username=gtme.username,
                        dev_username=bot.get_chat(IsDevloper()).username,
                    ),
                ),
                chat_id=message.chat.id,
                reply_markup=message_hi(),
            )

        if mtxt == "رجوع الى قسم رساله الترحيب":
            gtme = bot.get_me()
            bot.send_message(
                text=messagesBots.Welcome_message.format(
                    msg=Ismessage_join_member(),
                    bot_name=gtme.first_name,
                    bot_username=gtme.username,
                    dev_username=bot.get_chat(IsDevloper()).username,
                ),
                chat_id=message.chat.id,
                reply_markup=message_hi(),
            )

        if mtxt == "تعيين رساله الترحيب":
            bot.send_message(
                text="ارسل كليشه رساله الترحيب الان: ",
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, sign_message_join_member)

        if mtxt == "مسح رساله الترحيب":
            bot.send_message(
                text="- تم حذف رساله الترحيب 💞",
                chat_id=message.chat.id,
                reply_markup=message_hi(),
            )
            deleteMessage_join_member()

        if mtxt == "الادمينة":
            bot.send_message(
                text="اهلا بك في لوحة الخاصة بالادمينة",
                chat_id=message.chat.id,
                reply_markup=AdminsSitting(),
            )

        if mtxt == "رجوع الى قسم الادمينه":
            bot.send_message(
                text="اهلا بك في لوحة الخاصة بالادمينة",
                chat_id=message.chat.id,
                reply_markup=AdminsSitting(),
            )

        if mtxt == "عرض الادمينة":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم الادمينه"))
            bot.send_message(
                text=show_admin_markup(), chat_id=message.chat.id, reply_markup=mrk
            )
        if mtxt == "اضف ادمن":
            bot.send_message(
                text="حسنا, لكي يتم اضافة المستخدم الى قائمه الادمينة يجب ان يرسل \start الى البوت\n و من ثم يتم اضافته \n ارسل ايدي المستخدم هنا",
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, AddAdminsToBot)
        if mtxt == "تغيير المطور":
            bot.send_message(
                text="حسنا, لكي يتم تغيير المطور   يجب ان يرسل \start الى البوت\n و من ثم يتم اضافته \n ارسل ايدي المستخدم هنا",
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, AddDevlopToBot)

        if mtxt == "مسح ادمن":
            bot.send_message(
                text="ارسل ايدي الادمن هنا",
                chat_id=message.chat.id,
            )
            bot.register_next_step_handler(message, SendingUserNmaeAdmin)

        if mtxt == "المحظورين":
            bot.send_message(
                text="اهلا بك في لوحة الخاصة بالمحظورين",
                chat_id=message.chat.id,
                reply_markup=MutedSitting(),
            )

        if mtxt == "رجوع الى قسم المحظورين":
            bot.send_message(
                text="اهلا بك في لوحة الخاصة بالمحظورين",
                chat_id=message.chat.id,
                reply_markup=MutedSitting(),
            )

        if mtxt == "مسح محظور":
            bot.send_message(
                text="ارسل ايدي المحظور",
                chat_id=message.chat.id,
                reply_markup=MutedSitting(),
            )
            bot.register_next_step_handler(message, SendingUserNmaeMuted)

        if mtxt == "عرض المحظورين":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم المحظورين"))
            bot.send_message(
                text=show_muted_markup(), chat_id=message.chat.id, reply_markup=mrk
            )

        if mtxt == "الاحصائيات":
            bot.send_message(
                text="؟حدد نوع الاحصائيات",
                chat_id=message.chat.id,
                reply_markup=Edit_all(),
            )
        if mtxt == "رجوع الى قسم الاحصائيات":
            bot.send_message(
                text="؟حدد نوع الاحصائيات",
                chat_id=message.chat.id,
                reply_markup=Edit_all(),
            )

        if mtxt == "الاعضاء":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم الاحصائيات"))
            LEnght = show_user_markup()
            tx = "عدد الاعضاء المشتركين في بوتك الخاص هم: " + str(LEnght)
            bot.send_message(text=tx, chat_id=message.chat.id, reply_markup=mrk)

        if mtxt == "الكروبات":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="رجوع الى قسم الاحصائيات"))
            LEnght = len(show_all_groups().items())
            tx = "عدد المجاميع التي يوجود فيها بوتك الخاص هي: " + str(LEnght)
            bot.send_message(text=tx, chat_id=message.chat.id, reply_markup=mrk)

        if mtxt == "الاذاعة":
            tx = "حدد نوع الاذاعة؟"
            bot.send_message(text=tx, chat_id=message.chat.id, reply_markup=Broadcast())

        if mtxt == "العودة":
            tx = "حدد نوع الاذاعة؟"
            bot.send_message(text=tx, chat_id=message.chat.id, reply_markup=Broadcast())

        if mtxt == "اذاعه للاعضاء":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="الغاء الاذاعه"))
            bot.send_message(
                text="حسنًا ، أرسل الآن الرسالة: ",
                chat_id=message.chat.id,
                reply_markup=mrk,
            )
            bot.register_next_step_handler(message, SendBroadCast_to_members)
        if mtxt == "اذاعه للمجاميع":
            mrk = ReplyKeyboardMarkup()
            mrk.add(KeyboardButton(text="الغاء الاذاعه"))
            bot.send_message(
                text="حسنًا ، أرسل الآن الرسالة: ",
                chat_id=message.chat.id,
                reply_markup=mrk,
            )
            bot.register_next_step_handler(message, SendBroadCast_to_groups)

    else:
        if Ischannell() != "None":
            if IN_channel(Ischannell(), message.from_user.id):
                join_members(message=message)
            else:
                must_sub(
                    bot,
                    message,
                    Ischannell(),
                    InlineKeyboardMarkup,
                    InlineKeyboardButton,
                )
        else:
            join_members(message=message)


def back_to_main():
    mrk = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton(text=". رجوع .", callback_data="back_to_main")
    mrk.add(btn)
    return mrk


def back_to_must_sub():
    mrk = ReplyKeyboardMarkup(row_width=1)
    mrk.add(KeyboardButton(text="الرجوع الى قسم الاشتراك الاجباري"))
    return mrk


def message_hi():
    mrk = ReplyKeyboardMarkup(row_width=2)
    btns = [
        KeyboardButton(text="مسح رساله الترحيب"),
        KeyboardButton(text="تعيين رساله الترحيب"),
        KeyboardButton(text=". رجوع ."),
    ]
    mrk.add(*btns)
    return mrk


def back_to_message_join_member():
    mrk = ReplyKeyboardMarkup(row_width=1)
    btn = KeyboardButton(text="رجوع الى قسم رساله الترحيب")
    mrk.add(btn)
    return mrk


def reply_message(message):
    bot.send_message(
        message.chat.id,
        Decor("تم ارسال رسالتگ :)", "b"),
        reply_to_message_id=message.i,
        parse_mode="HTML",
    )


# @bot.callback_query_handler(func=lambda call: True, chat_types=["private"])
def CallBack_query(call: types.CallbackQuery):
    global chid
    chid = [call.message.chat.id, call.message.id]
    data = call.data

    if data == "reply to":
        bot.send_message(
            chat_id=call.message.chat.id,
            text=Decor("حسنا, الان يمكنك الرد على رساله المستخدم: ", "b"),
            reply_to_message_id=call.message.id,
            parse_mode="HTML",
        )
        bot.register_next_step_handler(call.message, xyz)


def show_user_markup():
    JH = [
        user_id["user_id"]
        for user_id in User_private.display_all_users_privte().values()
        if user_id["is_member"]
    ]

    return len(JH)


def Send_bc_gr_one():
    mark = InlineKeyboardMarkup()
    btns = []
    if not len(show_all_groups().items()):
        btn = InlineKeyboardButton(
            text="ماكو اي شي", callback_data="there is not any things"
        )
        btns.append(btn)
    else:
        for chat_id in show_all_groups().values():
            chat_id = chat_id["chat_id"]
            btn = InlineKeyboardButton(text=chat_id, callback_data=f"bc1 {chat_id}")
            btns.append(btn)
    mark.add(*btns)
    return mark


def show_admin_markup():
    txt = "هذه القائمة الخاصة بأحصائيات الادمينة" + "\n \n"
    a = 1
    for user_id in show_admins_bots():
        txt += f"Num[{a}] {user_id} \n"

    return txt


def show_muted_markup():
    txt = "هذه القائمة الخاصة بأحصائيات المحظورين" + "\n \n"
    users_ids = [
        user_id["user_id"]
        for user_id in User_private.display_all_users_privte().values()
        if user_id["is_blocked"]
    ]
    txt += f"عدد المحظورين = {len(users_ids)}"

    return txt


def AddAdminsToBot(message: Message):
    mrk = ReplyKeyboardMarkup()
    mrk.add(KeyboardButton(text="رجوع الى قسم الادمينه"))
    if IsDevloper() == message.from_user.id:
        IsOrNot = False
        USER = None
        for user_id in [
            user_id["user_id"]
            for user_id in User_private.display_all_users_privte().values()
            if user_id["is_member"]
        ]:
            if message.text == str(user_id):
                USER = user_id
                IsOrNot = True
        if not IsOrNot:
            bot.send_message(
                message.chat.id,
                Decor("المستخدم غير موجود في قائمة الاعضاء", "b"),
                reply_to_message_id=message.id,
                parse_mode="HTML",
                reply_markup=mrk,
            )

        else:
            bot.send_message(
                message.chat.id,
                Decor("تم اضافه المستخدم الى قائمه الادمينة", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=mrk,
            )
            try:
                bot.send_message(
                    USER,
                    Decor("مبروك, تم اضافتك الى الادمينة ,", "b"),
                    parse_mode="HTML",
                )
            except:
                pass
            User_private.update_user_private(
                IsDevloper(), USER, is_member=False, is_admin=True
            )
    else:
        bot.send_message(
            message.chat.id,
            Decor("هذا لامر مخصص  للمطور ", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
            reply_markup=mrk,
        )


def AddDevlopToBot(message: Message):
    mrk = ReplyKeyboardMarkup()
    mrk.add(KeyboardButton(text="رجوع الى قسم الادمينه"))
    if IsDevloper() == message.from_user.id:
        IsOrNot = False
        USER = None
        for user_id in [
            user_id["user_id"]
            for user_id in User_private.display_all_users_privte().values()
            if user_id["is_member"]
        ]:
            if message.text == str(user_id):
                USER = user_id
                IsOrNot = True
        if not IsOrNot:
            bot.send_message(
                message.chat.id,
                Decor("المستخدم غير موجود في قائمة الاعضاء", "b"),
                reply_to_message_id=message.id,
                parse_mode="HTML",
                reply_markup=mrk,
            )

        else:
            bot.send_message(
                message.chat.id,
                Decor("تم تغيير المطور ", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=mrk,
            )
            try:
                bot.send_message(
                    USER,
                    Decor("مبروك, لقد اصبحت الان مطور البوت ,", "b"),
                    parse_mode="HTML",
                )
            except:
                pass
            update_dev(USER)
    else:
        bot.send_message(
            message.chat.id,
            Decor("هذا لامر مخصص  للمطور ", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
            reply_markup=mrk,
        )


def SendingUserNmaeMuted(message: Message):
    mrk = ReplyKeyboardMarkup()
    mrk.add(KeyboardButton(text="رجوع الى قسم المحظورين"))
    IsOrNot = False
    USER = None
    for user_id in [
        user_id["user_id"]
        for user_id in User_private.display_all_users_privte().values()
        if user_id["is_blocked"]
    ]:
        if message.text == user_id:
            USER = user_id
            IsOrNot = True
    if not IsOrNot:
        bot.send_message(
            message.chat.id,
            Decor("المستخدم غير موجود في قائمة المحظورين", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
            reply_markup=mrk,
        )

    else:
        bot.send_message(
            message.chat.id,
            Decor("تم حذف المستخدم من قائمه المحظورين", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
            reply_markup=mrk,
        )
        try:
            bot.send_message(
                USER,
                Decor("مبروك, تم الغاء الحظر عن حسابك,", "b"),
                parse_mode="HTML",
            )
        except:
            pass
        User_private.update_user_private(
            IsDevloper(), USER, is_blocked=False, is_member=True
        )


def SendingUserNmaeAdmin(message: Message):
    mrk = ReplyKeyboardMarkup()
    mrk.add(KeyboardButton(text="رجوع الى قسم الادمينه"))
    if IsDevloper() == message.from_user.id:
        IsOrNot = False
        USER = None
        for user in [
            user_id["user_id"]
            for user_id in User_private.display_all_users_privte().values()
            if user_id["is_admin"]
        ]:
            if message.text == str(user) and user != message.from_user.id:
                USER = user
                IsOrNot = True
        if not IsOrNot:
            bot.send_message(
                message.chat.id,
                Decor("المستخدم غير موجود في قائمة الادمينه", "b"),
                reply_to_message_id=message.id,
                parse_mode="HTML",
                reply_markup=mrk,
            )

        else:
            bot.send_message(
                message.chat.id,
                Decor("تم حذف المستخدم من قائمه الادمينة", "b"),
                reply_to_message_id=message.id,
                parse_mode="HTML",
                reply_markup=mrk,
            )
            try:
                bot.send_message(
                    USER,
                    Decor("نأسف, تم ازالتك من قائمه الادمينة,", "b"),
                    parse_mode="HTML",
                )
            except:
                pass

            User_private.update_user_private(
                IsDevloper(), USER, is_member=True, is_admin=False
            )
    else:
        bot.send_message(
            message.chat.id,
            Decor("هذا لامر مخصص  للمطور ", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
            reply_markup=mrk,
        )


def U8(message: Message, Ab):
    AB = Ab

    def Suc():
        pass

    ty = message.content_type
    if ty == "text":
        tx = message.text
        try:
            bot.send_message(AB, tx)
            Suc()
        except:
            pass

    elif ty == "photo":
        tx = message.photo[0].file_id
        x = message.caption
        try:
            bot.send_photo(AB, tx, caption=x)
            Suc()
        except:
            pass

    elif ty == "voice":
        tx = message.voice.file_id
        x = message.caption
        try:
            bot.send_voice(AB, tx, caption=x)
            Suc()
        except:
            pass

    elif ty == "video":
        tx = message.video.file_id
        x = message.caption
        try:
            bot.send_video(AB, tx, caption=x)
            Suc()
        except:
            pass

    elif ty == "video":
        tx = message.video.file_id
        x = message.caption
        try:
            bot.send_video(AB, tx, caption=x)
            Suc()
        except:
            pass

    elif ty == "animation":
        tx = message.animation.file_id
        x = message.caption
        try:
            bot.send_animation(AB, tx, caption=x)
            Suc()
        except:
            pass

    elif ty == "sticker":
        tx = message.sticker.file_id
        try:
            bot.send_sticker(AB, tx)
            Suc()
        except:
            pass


def Edit_all():
    keyboard = ReplyKeyboardMarkup(row_width=2)
    List_btns = [
        KeyboardButton(text="الاعضاء"),
        KeyboardButton(text="الكروبات"),
        KeyboardButton(text=". رجوع ."),
    ]
    keyboard.add(*List_btns)
    return keyboard


def Add_Public_responses(message: Message):
    global r_m_n
    r_m_n = message
    if message.content_type == "text":
        bot.send_message(message.chat.id, "ارسل الرد:")
        bot.register_next_step_handler(message, Add_Public_responses2)


def Add_Public_responses2(message: Message):
    if message.content_type == "text":
        bot.send_message(message.chat.id, "تم حفظ الرد")
        Add_general_response_to_the_bot(r_m_n.text, message.text)


def Del_Public_responses(message: Message):
    if message.content_type == "text":
        bot.send_message(message.chat.id, "تم حذف الرد")
        Del_general_response_fromBOT(message.text)


def Sho_Public_responses(message: Message):
    if message.content_type == "text":
        bot.send_message(
            message.chat.id,
            text=" ".join(Display_generic_response_to_the_bot(message.text)),
        )


def SendBroadCast_to_members(message):
    msg = message.text
    a, b = 1, 0
    Member_keys = []
    for user_id in [
        user_id["user_id"]
        for user_id in User_private.display_all_users_privte().values()
        if user_id["is_member"]
    ]:
        try:
            U8(message, user_id)
            a += 1
        except:
            Member_keys.append(user_id)
            try:
                bot.leave_chat(user_id)
            except:
                pass
            b += 1
    Kill_key(Member_keys)
    m = bot.send_message(
        chat_id=message.chat.id,
        text="تم ارسال اذاعة الى اعضائك يمكنك الان العودة",
        reply_markup=View_statistics(a, b),
    )


def SendBroadCast_to_groups(message):
    msg = message.text
    a, b = 0, 0
    Groups_keys = []
    for user in show_all_groups_ids().values():
        try:
            U8(message, user["chat_id"])
            a += 1
        except Exception as e:
            Groups_keys.append(user["chat_id"])
            try:
                bot.leave_chat(user["chat_id"])
            except:
                pass

            b += 1
    Kill_key_gr(Groups_keys)
    m = bot.send_message(
        chat_id=message.chat.id,
        text="تم ارسال اذاعة الى كروباتك يمكنك الان العودة",
        reply_markup=View_statistics(a, b),
    )
    mrk = ReplyKeyboardMarkup()
    mrk.add(KeyboardButton(text="العودة"))
    bot.send_message(message.chat.id, text="~", reply_markup=mrk)


def Kill_key(List: list):
    for ids in List:
        User_private.update_user_private(IsDevloper(), ids, is_member=False)


def Kill_key_gr(List: list):
    for ids in List:
        delete_group(ids)


def View_statistics(a, b):
    keyboard = InlineKeyboardMarkup(row_width=2)
    List_btns = [
        InlineKeyboardButton(text=f"النجاح: {a}", callback_data="succ_bc"),
        InlineKeyboardButton(text=f"الفشل: {b}", callback_data="failed"),
        InlineKeyboardButton(text="اللوبي", callback_data="lopy"),
    ]
    keyboard.add(*List_btns)
    return keyboard


def lopy():
    keyboard = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text="اللوبي", callback_data="lopy")
    keyboard.add(btn)
    return keyboard


def xyz(message: types.Message):
    text = message.text
    if text == "حظر":
        bot.send_message(
            IsDevloper(),
            text=Decor("تم حظر المستخدم بنجاح,,,", "b"),
            reply_to_message_id=message.id,
            parse_mode="HTML",
        )
        bot.send_message(
            senderMsg[0].id,
            text=Decor("تم حظرك, بسبب اسلوبك النابي.", "b"),
            parse_mode="HTML",
        )
        user = senderMsg[0]
        User_private.update_user_private(
            IsDevloper(), user.id, is_blocked=False, is_member=False
        )

    else:
        bot.edit_message_reply_markup(chid[0], chid[1])
        bot.send_message(
            senderMsg[0].id,
            text=Decor(f"الرد: {message.text}", "b"),
            reply_to_message_id=senderMsg[1],
            parse_mode="HTML",
        )


def sign_message_join_member(message):
    bot.send_message(
        message.chat.id,
        text=Decor("- تم حفظ رساله الترحيب ❤", "b"),
        parse_mode="HTML",
        reply_to_message_id=message.id,
        reply_markup=back_to_message_join_member(),
    )
    update_message_join_member(message.text)


def sign_chanell(message: types.Message):
    if not (message.forward_from_chat):
        if IN_channel(message.text, bot.get_me().id):
            bot.send_message(
                message.chat.id,
                text=Decor("- تم حفظ القناه ❤", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=back_to_must_sub(),
            )
            chid = bot.get_chat(message.text).id
            update_chanell(chid)
        else:
            bot.send_message(
                message.chat.id,
                text=Decor("البوت ليس ادمن في القناه 💢", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=back_to_must_sub(),
            )
    else:
        if message.forward_from_chat.type == "channel":
            try:
                chid = message.forward_from_chat
                id = chid.id
                if "admin" in bot.get_chat_member(id, bot.get_me().id).status:
                    bot.send_message(
                        message.chat.id,
                        "<b> تمت اضافة القناة الى البوت 🎀 </b>",
                        reply_to_message_id=message.id,
                        reply_markup=back_to_must_sub(),
                    )
                    update_chanell(id)
                else:
                    bot.send_message(
                        message.chat.id,
                        "<b> البوت ليس ادمن في القناة! </b>",
                        reply_to_message_id=message.id,
                        reply_markup=back_to_must_sub(),
                    )
            except:
                bot.send_message(
                    message.chat.id,
                    "<b> البوت ليس ادمن في القناة! </b>",
                    reply_to_message_id=message.id,
                    reply_markup=back_to_must_sub(),
                )
        else:
            bot.send_message(
                message.chat.id,
                "<b> الرسالة ليست محولة من قناة! </b>",
                reply_to_message_id=message.id,
                reply_markup=back_to_must_sub(),
            )


def Add_chanell_global_replay(message: types.Message):
    if not (message.forward_from_chat):
        if IN_channel(message.text, bot.get_me().id):
            bot.send_message(
                message.chat.id,
                text=Decor("- تم حفظ القناه ❤", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=Chanell_Public_responses(),
            )
            chid = bot.get_chat(message.text).id
            update_Chanell_reply_golbal(chid)
        else:
            bot.send_message(
                message.chat.id,
                text=Decor("البوت ليس ادمن في القناه 💢", "b"),
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=Chanell_Public_responses(),
            )
    else:
        if message.forward_from_chat.type == "channel":
            try:
                chid = message.forward_from_chat
                id = chid.id
                if "admin" in bot.get_chat_member(id, bot.get_me().id).status:
                    bot.send_message(
                        message.chat.id,
                        "<b> تمت اضافة القناة الى البوت 🎀 </b>",
                        reply_to_message_id=message.id,
                        reply_markup=Chanell_Public_responses(),
                    )
                    update_Chanell_reply_golbal(id)
                else:
                    bot.send_message(
                        message.chat.id,
                        "<b> البوت ليس ادمن في القناة! </b>",
                        reply_to_message_id=message.id,
                        reply_markup=Chanell_Public_responses(),
                    )
            except:
                bot.send_message(
                    message.chat.id,
                    "<b> البوت ليس ادمن في القناة! </b>",
                    reply_to_message_id=message.id,
                    reply_markup=Chanell_Public_responses(),
                )
        else:
            bot.send_message(
                message.chat.id,
                "<b> الرسالة ليست محولة من قناة! </b>",
                reply_to_message_id=message.id,
                reply_markup=Chanell_Public_responses(),
            )


def sign_message(message: types.Message):
    bot.send_message(
        message.chat.id,
        text=Decor("- تم حفظ الرسالة ❤", "b"),
        parse_mode="HTML",
        reply_to_message_id=message.id,
        reply_markup=back_to_must_sub(),
    )
    update_message(message.text)


# keep_alive()

print("\033[92m")


def reply_mrk():
    m = InlineKeyboardMarkup()
    b = InlineKeyboardButton(text="رد", callback_data="reply to")
    m.add(b)
    return m


print(messagesBots.copy_right)

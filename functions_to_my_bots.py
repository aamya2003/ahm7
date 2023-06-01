import telebot
from telebot.types import *
from database_main import *
import re, messagesBots
import string
import requests
from messagesBots import *

# My_id = IsDevloper()

import config

bot = telebot.TeleBot(config.Token)


def Compulsory_subscription(message: Message):
    if Ischannell() != "None":
        user_id = message.from_user.id
        Get_chat_member_ststus = bot.get_chat_member(Ischannell(), user_id).status
        if Get_chat_member_ststus in ["member", "creator", "administrator"]:
            return True
        else:

            def main_mark():
                invite = bot.create_chat_invite_link(Ischannell())
                InviteLink = invite.invite_link
                mrkplink = InlineKeyboardMarkup()
                mrkplink.add(
                    InlineKeyboardButton(
                        bot.get_chat(Ischannell()).title, url=InviteLink
                    )
                )
                return mrkplink

            bot.send_message(
                message.chat.id,
                Ismessage(),
                reply_markup=main_mark(),
                reply_to_message_id=message.id,
            )
            return False
    else:
        return True


def IN_channel(chat_id, user_id):
    url = f"https://api.telegram.org/bot{config.Token}/getChatMember?chat_id={chat_id}&user_id={user_id}"
    req = requests.get(url).json()
    if "result" in req:
        if req["result"]["status"] in ["member", "creator", "administrator"]:
            return True
        else:
            return False
    else:
        return False


def Automatic_lift(Chat_id):
    allAdminsss = bot.get_chat_administrators(Chat_id)

    Admins = [Admin.user for Admin in allAdminsss if not Admin.user.is_bot]
    for adimn in Admins:
        insert_user(Chat_id, adimn.id)
        status = bot.get_chat_member(Chat_id, adimn.id).status
        if status == "creator":
            update_user(Chat_id, adimn.id, rank_user="bulder")

        if adimn.id == IsDevloper():
            update_user(Chat_id, adimn.id, rank_user="programer")

        else:
            update_user(Chat_id, adimn.id, rank_user="reeve")


def Sigin_user(message: Message):
    chat_id = message.chat.id
    if message.reply_to_message:
        user_id_1 = message.from_user.id
        user_id_2 = message.reply_to_message.from_user.id
        insert_user(chat_id, user_id_1)
        insert_user(chat_id, user_id_2)

    elif message.forward_from_chat:
        user_id_1 = message.from_user.id
        user_id_2 = message.forward_from_chat.from_user.id
        insert_user(chat_id, user_id_1)
        insert_user(chat_id, user_id_2)
    else:
        insert_user(chat_id, message.from_user.id)


def Get_rank(chat_id, user_id):
    return Get_rank_user(chat_id, user_id)


def all_pre(bot, chat_id):
    info = bot.get_chat_member(chat_id, bot.get_me().id)
    change = bool(info.can_change_info)
    pin = bool(info.can_pin_messages)
    delete = bool(info.can_delete_messages)
    pan = bool(info.can_restrict_members)
    add = bool(info.can_promote_members)
    invite = bool(info.can_invite_users)
    mng = bool(info.can_manage_video_chats) + bool(info.can_manage_voice_chats)
    all = change + pin + delete + pan + add + invite + mng
    if all == 8:
        return True
    else:
        return False


def Persian(word):
    # persian_pattern = re.compile("[\u0600-\u06FF]+")
    # if persian_pattern.search(word):
    #     return True
    # else:
    #     return False
    List_persian = ["چ", "هڤ", "ڨ", "گ", "پ", "ڜ", "ژ"]
    Loping = []
    for w in word:
        if w in List_persian:
            Loping.append(w)
    if len(Loping) > 0:
        return True
    else:
        return False


def Get_prerson(name, id):
    mrk = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text=name, callback_data=id)
    mrk.add(btn)
    return mrk


def Links_word(word):
    # Sample string with links
    string_with_links = word

    # Regular expression pattern to match links
    link_pattern = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    )

    # Find all links in the string
    links = re.findall(link_pattern, string_with_links)

    return links


def English_words(word):
    List_en = []
    for i in word:
        if i in string.ascii_letters:
            List_en.append(i)
    if len(List_en) != 0:
        return True
    return False


def Tag_per(word):
    if "@" in word:
        return True
    else:
        return False


def Sharihaa(word):
    if "/" in word:
        return True
    else:
        return False


def conItU(text: str, chat_id, user_id):
    gtcm = bot.get_chat_member(chat_id, user_id).user
    text = text.replace("#name", gtcm.first_name)
    text = text.replace("#id", str(gtcm.id))
    text = text.replace("#username", gtcm.username)
    return text


def Bottom_channel_link():
    if Ischannell() != "None":
        ch = bot.get_chat(Ischannell())
        mr = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=ch.title, url="https://t.me/" + ch.username)]]
        )
        return mr
    else:
        return None


def save_replies_into_db(name, repl: Message):
    ch = repl.chat.id
    if repl.text:
        insert_rep(ch, name, repl.text)

    if repl.photo:
        file_info = bot.get_file(repl.photo[2].file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_photo_message_rep.jpg"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.video:
        file_info = bot.get_file(repl.video.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_video_message_rep.mp4"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.voice:
        file_info = bot.get_file(repl.voice.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_voice_message_rep.mp3"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.audio:
        file_info = bot.get_file(repl.audio.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_audio_message_rep.mp3"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.video_note:
        file_info = bot.get_file(repl.video_note.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_video_note_message_rep.mp4"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.document:
        file_info = bot.get_file(repl.document.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_document_message_rep.txt"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.animation:
        file_info = bot.get_file(repl.animation.file_id)
        file = bot.download_file(file_info.file_path)
        nf = f"{name}_{repl.chat.id}_animation_message_rep.mp4"
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)

    if repl.sticker:
        file_info = bot.get_file(repl.sticker.file_id)
        file = bot.download_file(file_info.file_path)
        nf = (
            f"{name}_{repl.chat.id}_sticker_message_rep."
            + file_info.file_path.split(".")[-1]
        )
        with open(nf, "wb") as f:
            f.write(file)
            insert_rep(ch, name, nf, repl.caption)


def ShowAllRep_Group(chat_id):
    rps = {}
    a = 0
    for rep in show_all_reps_grps(chat_id).values():
        name = rep["name"]
        reply = rep["reply"]
        typ = ""
        if reply.endswith(".mp3"):
            typ = "صوت"

        elif reply.endswith(".mp4"):
            typ = "فيديو"

        elif reply.endswith(".jpg"):
            typ = "صوره"

        elif reply.endswith(".png"):
            typ = "ملصق"

        elif reply.endswith(".txt"):
            typ = "ملف"

        else:
            typ = "نص"

        rps.update({str(a): {"name": name, "type": typ}})
        a += 1
    return rps


def Type_reply_return(Reply, message: Message):
    r = Reply["rep"]
    t = Reply["txt_rep"]
    if r.endswith(".mp4"):
        bot.send_video(
            message.chat.id,
            open(r, "rb"),
            caption=conItU(t, message.chat.id, message.from_user.id),
            reply_to_message_id=message.id,
        )

    elif r.endswith(".mp3"):
        bot.send_audio(
            message.chat.id,
            open(r, "rb"),
            caption=conItU(t, message.chat.id, message.from_user.id),
            reply_to_message_id=message.id,
        )

    elif r.endswith(".jpg"):
        bot.send_photo(
            message.chat.id,
            open(r, "rb"),
            caption=conItU(t, message.chat.id, message.from_user.id),
            reply_to_message_id=message.id,
        )

    elif r.endswith(".webp"):
        bot.send_sticker(
            message.chat.id,
            open(r, "rb"),
            reply_to_message_id=message.id,
        )

    elif r.endswith(".webm"):
        bot.send_sticker(
            message.chat.id,
            open(r, "rb"),
            reply_to_message_id=message.id,
        )
    elif r.endswith(".tgs"):
        bot.send_sticker(
            message.chat.id,
            open(r, "rb"),
            reply_to_message_id=message.id,
        )
    elif r.endswith(".png"):
        bot.send_sticker(
            message.chat.id,
            open(r, "rb"),
            reply_to_message_id=message.id,
        )

    elif r.endswith(".txt"):
        bot.send_document(
            message.chat.id,
            open(r, "rb"),
            caption=conItU(t, message.chat.id, message.from_user.id),
            reply_to_message_id=message.id,
        )
    else:
        bot.send_message(message.chat.id, r, reply_to_message_id=message.id)


def convertRank2Ar(rank):
    if rank == "member":
        return "عضو"

    elif rank == "distinct":
        return "مميز"

    elif rank == "admin":
        return "ادمن"

    elif rank == "programmer":
        return "مطور اساسي"

    elif rank == "reeve":
        return "مدير"

    elif rank == "creator2":
        return "منشئ ثانوي"

    elif rank == "creator":
        return "منشئ"

    elif rank == "owner2":
        return "مالك ثانوي"

    elif rank == "owner":
        return "مالك"

    elif rank == "devloper2":
        return "مطور ثانوي"

    elif rank == "devloper":
        return "مطور"

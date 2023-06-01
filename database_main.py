import shelve, sqlite3, threading, messagesBots, random
from datetime import datetime
from telebot.types import *

Group_name_file = "group.db"
Users_name_file = "users.db"
Vandals_name_file = "vandals.db"
Bot_name_file = "bots.db"
Reps_name_file = "reps.db"
general_response_name_file = "general_responses.db"
User_private_name_file = "User_private.db"
general_response = "general_responsesBOT.db"
lock = threading.Lock()
My_id = int("5832988930")
db = sqlite3.connect("Towasoul.db", check_same_thread=False)
cr = db.cursor()


class User:
    def __init__(
        self,
        chat_id,
        user_id,
        points=0,
        msgs=0,
        shgs=0,
        directs=0,
        rank_user="member",
        nickname=None,
        time_joined=None,
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.points = points
        self.msgs = msgs
        self.shgs = shgs
        self.rank_user = rank_user
        self.directs = directs
        self.nickname = nickname
        self.time_joined = time_joined or datetime.now()


# حفظ المستخدم
def insert_user(chat_id, user_id):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" not in db:
            db[f"{chat_id}_{user_id}"] = User(chat_id, user_id)


# تحديث المستخدم تختار اي وحده اما قيمه واحده او عده قيم
# update_user(28727272727, 73773737, points=1000)
# update_user(28727272727, 73773737, points=1000, msgs= 8)
# update_user(28727272727, 73773737, rank_user= "member") رتبته المستخدم
def update_user(
    chat_id,
    user_id,
    points=None,
    msgs=None,
    rank_user=None,
    shgs=None,
    directs=None,
    nickname=None,
):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" in db:
            user = db[f"{chat_id}_{user_id}"]
            if points is not None:
                user.points += points
            if msgs is not None:
                user.msgs += msgs
            if rank_user is not None:
                user.rank_user = rank_user
            if directs is not None:
                user.directs = directs
            if nickname is not None:
                user.nickname = nickname
            db[f"{chat_id}_{user_id}"] = user
            if shgs is not None:
                user.shgs += shgs
            db[f"{chat_id}_{user_id}"] = user


def deleteUserProperty(
    chat_id,
    user_id,
    points=None,
    msgs=None,
    shgs=None,
):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" in db:
            user = db[f"{chat_id}_{user_id}"]
            if points is not None:
                user.points = 0
            if msgs is not None:
                user.msgs = 0

            db[f"{chat_id}_{user_id}"] = user

            if shgs is not None:
                user.shgs = 0
            db[f"{chat_id}_{user_id}"] = user


# حذف المسخدم من القاعده
def delete_user(chat_id, user_id):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" in db:
            del db[f"{chat_id}_{user_id}"]


# تصفير بيانات المستخدم
def delete_msgs_points(chat_id, user_id):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" in db:
            user = db[f"{chat_id}_{user_id}"]
            user.points = 0
            user.msgs = 0
            db[f"{chat_id}_{user_id}"] = user


# عرض بيانات المستخدم
def show_user_info(chat_id, user_id):
    with shelve.open(Users_name_file) as db:
        if f"{chat_id}_{user_id}" in db:
            user = db[f"{chat_id}_{user_id}"]
            USER = {
                "chat_id": user.chat_id,
                "user_id": user.user_id,
                "points": user.points,
                "time_joined": user.time_joined,
                "rank": user.rank_user,
                "msgs": user.msgs,
                "shgs": user.shgs,
                "directs": user.directs,
                "nickname": user.nickname,
            }
            return USER if USER else None


# عرض جميع المسخدمين
def show_all_users():
    with shelve.open(Users_name_file) as db:
        users = {}
        for key in db:
            user = db[key]

            print(f"Chat ID: {user.chat_id}")
            print(f"User ID: {user.user_id}")
            print(f"Points: {user.points}")
            print(f"Messages: {user.msgs}")
            print(f"Rank: {user.rank_user}")
            print(f"Time Joined: {user.time_joined}")
            print("---")
        return users


# حذف جميع المستخدمين من كروبك فقط عن طيق ايدي الكروب
def Delete_users_by_chat_id(chat_id):
    with shelve.open(Users_name_file) as db:
        for key in db:
            user = db[key]
            delete_user(chat_id, user.user_id)


# حذف مستخدم من كروبك
def Delete_users_by_chat_id(chat_id):
    with shelve.open(Users_name_file) as db:
        for key in db:
            user = db[key]
            delete_user(chat_id, user.user_id)


# تنزيل جميع رتب المستخدمين في كروبك
def Download_all_ranks(chat_id):
    with shelve.open(Users_name_file) as db:
        for key in db:
            user = db[key]
            # if user.rank_user != "bulder" or user.rank_user != "programmer":
            update_user(
                chat_id, user.user_id, rank_user="member"
            ) if user.rank_user not in ["programmer", "bulder"] else print("Here")
            print(user.rank_user)


def programmer_user(user_id):
    if IsDevloper() == user_id or user_id in show_admins_bots():
        return True
    else:
        return False


# عرض رتبه المستخدم في كروبك
def Get_rank_user(chat_id, user_id):
    if programmer_user(user_id):
        return "programmer"
    else:
        return show_user_info(chat_id, user_id)["rank"]


def Get_nickname_user(chat_id, user_id):
    return show_user_info(chat_id, user_id)["nickname"]


"""







SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


class Group:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.towheed = None
        self.sendMessage = None
        self.SendPhoto = None
        self.SendVideo = None
        self.SendVoice = None
        self.SendSticer = None
        self.SendAnmation = None
        self.SendLinks = None
        self.SendEnglishWord = None
        self.SendParsionWord = None
        self.SendTag = None
        self.SendShariha = None
        self.SendChannel = None
        self.AddBots = None
        self.AddDirect = None
        self.SendFowrod = None
        self.EditMessage = None
        self.Sab = None
        self.Looping = None
        self.SendFiles = None
        self.JoinMember = None
        self.Pin = None
        self.show_PId = None
        self.show_id = None
        self.det_member = None
        self.games = None


def insert_group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id not in db:
            try:
                db[chat_id] = Group(chat_id)
            except:
                pass


def show_all_groups():
    with shelve.open(Group_name_file) as db:
        a = 0
        grs = {}
        for chat_id in db:
            if isinstance(db[chat_id], Group):
                group = db[chat_id]
                Grou = {
                    "sendMessage": group.sendMessage,
                    "SendPhoto": group.SendPhoto,
                    "SendVideo": group.SendVideo,
                    "SendVoice": group.SendVoice,
                    "SendSticer": group.SendSticer,
                    "SendAnmation": group.SendAnmation,
                    "SendLinks": group.SendLinks,
                    "SendEnglishWord": group.SendEnglishWord,
                    "SendParsionWord": group.SendParsionWord,
                    "SendTag": group.SendTag,
                    "SendShariha": group.SendShariha,
                    "SendChannel": group.SendChannel,
                    "AddBots": group.AddBots,
                    "AddDirect": group.AddDirect,
                    "SendFowrod": group.SendFowrod,
                    "EditMessage": group.EditMessage,
                    "Sab": group.Sab,
                    "towheed": group.towheed,
                    "Looping": group.Looping,
                    "SendFiles": group.SendFiles,
                    "JoinMember": group.JoinMember,
                    "Pin": group.Pin,
                    "show_PId": group.show_PId,
                    "show_id": group.show_id,
                    "det_member": group.det_member,
                    "games": group.games,
                }
                grs.update({str(a): Grou})
            a += 1
        return grs


def show_all_groups_ids():
    with shelve.open(Group_name_file) as db:
        a = 0
        grs = {}
        for chat_id in db:
            if isinstance(db[chat_id], Group):
                group = db[chat_id]
                Grou = {
                    "chat_id": group.chat_id,
                }
                grs.update({str(a): Grou})
            a += 1
        return grs


def delete_group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            del db[chat_id]


def show_group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            group = db[chat_id]
            Grou = {
                "sendMessage": group.sendMessage,
                "SendPhoto": group.SendPhoto,
                "SendVideo": group.SendVideo,
                "SendVoice": group.SendVoice,
                "SendSticer": group.SendSticer,
                "SendAnmation": group.SendAnmation,
                "SendLinks": group.SendLinks,
                "SendEnglishWord": group.SendEnglishWord,
                "SendParsionWord": group.SendParsionWord,
                "SendTag": group.SendTag,
                "SendShariha": group.SendShariha,
                "SendChannel": group.SendChannel,
                "AddBots": group.AddBots,
                "AddDirect": group.AddDirect,
                "SendFowrod": group.SendFowrod,
                "EditMessage": group.EditMessage,
                "Sab": group.Sab,
                "towheed": group.towheed,
                "Pin": group.Pin,
                "SendFiles": group.SendFiles,
                "JoinMember": group.JoinMember,
                "Looping": group.Looping,
                "show_PId": group.show_PId,
                "show_id": group.show_id,
                "det_member": group.det_member,
                "games": group.games,
            }
            return Grou


def check_group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            return True
        else:
            return False


def update_group(
    chat_id,
    towheed=None,
    sendMessage=None,
    SendPhoto=None,
    SendVideo=None,
    SendVoice=None,
    SendSticer=None,
    SendAnmation=None,
    SendLinks=None,
    SendEnglishWord=None,
    SendParsionWord=None,
    SendTag=None,
    SendShariha=None,
    SendChannel=None,
    AddBots=None,
    AddDirect=None,
    SendFowrod=None,
    EditMessage=None,
    Sab=None,
    Pin=None,
    SendFiles=None,
    JoinMember=None,
    Looping=None,
    show_PId=None,
    show_id=None,
    det_member=None,
    games=None,
):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            group = db[chat_id]

            if towheed is not None:
                group.towheed = towheed

            if sendMessage is not None:
                group.sendMessage = sendMessage

            if SendPhoto is not None:
                group.SendPhoto = SendPhoto

            if SendVideo is not None:
                group.SendVideo = SendVideo

            if SendVoice is not None:
                group.SendVoice = SendVoice

            if SendSticer is not None:
                group.SendSticer = SendSticer

            if SendAnmation is not None:
                group.SendAnmation = SendAnmation

            if SendLinks is not None:
                group.SendLinks = SendLinks

            if SendEnglishWord is not None:
                group.SendEnglishWord = SendEnglishWord

            if SendParsionWord is not None:
                group.SendParsionWord = SendParsionWord

            if SendTag is not None:
                group.SendTag = SendTag

            if SendShariha is not None:
                group.SendShariha = SendShariha

            if SendChannel is not None:
                group.SendChannel = SendChannel

            if AddBots is not None:
                group.AddBots = AddBots

            if AddDirect is not None:
                group.AddDirect = AddDirect

            if SendFowrod is not None:
                group.SendFowrod = SendFowrod

            if EditMessage is not None:
                group.EditMessage = EditMessage

            if Sab is not None:
                group.Sab = Sab

            if Pin is not None:
                group.Pin = Pin

            if Looping is not None:
                group.Looping = Looping

            if JoinMember is not None:
                group.JoinMember = JoinMember

            if SendFiles is not None:
                group.SendFiles = SendFiles

            if show_PId is not None:
                group.show_PId = show_PId

            if show_id is not None:
                group.show_id = show_id

            if det_member is not None:
                group.det_member = det_member
            if games is not None:
                group.games = games

            db[chat_id] = group

    with shelve.open(Group_name_file) as db:
        return chat_id in db and isinstance(db[chat_id], Group)


def UnLockAll_Group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            group = db[chat_id]

            group.towheed = True

            group.sendMessage = True

            group.SendPhoto = True

            group.SendVideo = True

            group.SendVoice = True

            group.SendSticer = True

            group.SendAnmation = True

            group.SendLinks = True

            group.SendEnglishWord = True

            group.SendParsionWord = True

            group.SendTag = True

            group.SendShariha = True

            group.SendChannel = True

            group.AddBots = True

            group.AddDirect = True

            group.SendFowrod = True

            group.EditMessage = True

            group.Sab = True

            group.Pin = True

            group.Looping = True

            group.JoinMember = True

            group.SendFiles = True

            # group.show_PId = True

            # group.show_id = True

            # group.det_member = True

            # group.games = True

            db[chat_id] = group
    with shelve.open(Group_name_file) as db:
        return chat_id in db and isinstance(db[chat_id], Group)


def LockAll_Group(chat_id):
    chat_id = str(chat_id)
    with shelve.open(Group_name_file) as db:
        if chat_id in db:
            group = db[chat_id]

            group.towheed = False

            group.sendMessage = False

            group.SendPhoto = False

            group.SendVideo = False

            group.SendVoice = False

            group.SendSticer = False

            group.SendAnmation = False

            group.SendLinks = False

            group.SendEnglishWord = False

            group.SendParsionWord = False

            group.SendTag = False

            group.SendShariha = False

            group.SendChannel = False

            group.AddBots = False

            group.AddDirect = False

            group.SendFowrod = False

            group.EditMessage = False

            group.Sab = False

            group.Pin = False

            group.Looping = False

            group.JoinMember = False

            group.SendFiles = False

            # group.show_PId = False

            # group.show_id = False

            # group.det_member = False

            # group.games = False

            db[chat_id] = group
    with shelve.open(Group_name_file) as db:
        return chat_id in db and isinstance(db[chat_id], Group)


def delete_all_groups():
    with shelve.open(Group_name_file) as db:
        for chat_id in list(db.keys()):
            if isinstance(db[chat_id], Group):
                del db[chat_id]


# UnLockAll_Group(-1001506632083)
# print(show_group(-1001506632083))


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


class MaliciousUser:
    def __init__(
        self, chat_id, user_id, is_banned=None, is_blocked=None, is_muted=None
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_banned = is_banned
        self.is_blocked = is_blocked
        self.is_muted = is_muted


class MaliciousUserDB:
    def __init__(self, db_file):
        self.db = shelve.open(db_file)

    def add_user(
        self, chat_id, user_id, is_banned=None, is_blocked=None, is_muted=None
    ):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]
            if is_banned is not None:
                user.is_banned = is_banned
            if is_blocked is not None:
                user.is_blocked = is_blocked
            if is_muted is not None:
                user.is_muted = is_muted
            user = MaliciousUser(chat_id, user_id, is_banned, is_blocked, is_muted)
        else:
            user = MaliciousUser(chat_id, user_id, is_banned, is_blocked, is_muted)
        self.db[key] = user

    def update_user(
        self, chat_id, user_id, is_banned=None, is_blocked=None, is_muted=None
    ):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]
            if is_banned is not None:
                user.is_banned = is_banned
            if is_blocked is not None:
                user.is_blocked = is_blocked
            if is_muted is not None:
                user.is_muted = is_muted
            self.db[key] = user

    def delete_user(self, chat_id, user_id):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            del self.db[key]

    def delete_users(self, chat_id, is_banned=None, is_blocked=None, is_muted=None):
        Listr = []
        for key in self.db:
            user = self.db[key]
            if user.chat_id == chat_id:
                if is_banned:
                    self.add_user(user.chat_id, user.user_id, is_banned=False)
                    Listr.append(user.user_id)
                if is_blocked:
                    self.add_user(user.chat_id, user.user_id, is_blocked=False)
                    Listr.append(user.user_id)
                if is_muted:
                    self.add_user(user.chat_id, user.user_id, is_muted=False)
        return Listr

    def display_users(self, is_banned=None, is_blocked=None, is_muted=None):
        a = 0
        users = {}
        for key in self.db:
            user = self.db[key]
            if (
                (is_banned is None or user.is_banned == is_banned)
                and (is_blocked is None or user.is_blocked == is_blocked)
                and (is_muted is None or user.is_muted == is_muted)
            ):
                USER = {
                    str(a): {
                        "chat_id": user.chat_id,
                        "user_id": user.user_id,
                        "is_blocked": user.is_blocked,
                        "is_banned": user.is_banned,
                        "is_muted": user.is_muted,
                    }
                }
                users.update(USER)
                a += 1
        return users

    def display_all_users(self):
        users = {}
        a = 0
        for key in self.db:
            user = self.db[key]
            USER = {
                str(a): {
                    "chat_id": user.chat_id,
                    "user_id": user.user_id,
                    "is_blocked": user.is_blocked,
                    "is_banned": user.is_banned,
                    "is_muted": user.is_muted,
                }
            }
            a += 1
            # print(USER)
            users.update(USER)
        return users

    def display_user_details(self, chat_id, user_id):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]
            USER = {
                "is_blocked": user.is_blocked,
                "is_banned": user.is_banned,
                "is_muted": user.is_muted,
            }
            return USER
        else:
            return None


Vandals = MaliciousUserDB(Vandals_name_file)


# Add a malicious user
# db.add_user("chat4", "user3", is_banned=True)
# db.add_user("chat", "user3", is_blocked=True)


# Update a malicious user
# db.update_user("chat1", "user1", is_muted=True)


# Delete a malicious user
# db.delete_user("chat1", "user1")


# Delete malicious users by status
# db.delete_users(is_banned=True)


# Display malicious users by status


# db.display_users(is_banned=True)


# Display user details
# det = Vandals.display_user_details(1, 7)


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


def insert_bot_name():
    with shelve.open(Bot_name_file) as db:
        if "name_bot" not in db:
            db["name_bot"] = "bot"


def insert_devloper_id():
    with shelve.open(Bot_name_file) as db:
        if "devloper_id" not in db:
            db["devloper_id"] = My_id


def update_dev(dev_id):
    with shelve.open(Bot_name_file) as db:
        if f"devloper_id" in db:
            db[f"devloper_id"] = dev_id


def delete_bot_name():
    with shelve.open(Bot_name_file) as db:
        if f"name_bot" in db:
            del db[f"name_bot"]


def show_bot_name():
    with shelve.open(Bot_name_file) as db:
        if f"name_bot" in db:
            return db[f"name_bot"]
        else:
            return None


def IsDevloper():
    with shelve.open(Bot_name_file) as db:
        if f"devloper_id" in db:
            return db[f"devloper_id"]
        else:
            return "None"


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


class Rep:
    def __init__(
        self,
        chat_id,
        name_rep,
        rep,
        txt_rep="",
    ):
        self.chat_id = chat_id
        self.name_rep = name_rep
        self.rep = rep
        self.txt_rep = txt_rep


def insert_rep(chat_id, name_rep, rep, txt_rep=""):
    with shelve.open(Reps_name_file) as db:
        db[f"{chat_id}_{name_rep}"] = Rep(chat_id, name_rep, rep, txt_rep)


def delete_rep(chat_id, name_rep):
    with shelve.open(Reps_name_file) as db:
        if f"{chat_id}_{name_rep}" in db:
            del db[f"{chat_id}_{name_rep}"]


def show_rep_info(chat_id, name_rep):
    with shelve.open(Reps_name_file) as db:
        if f"{chat_id}_{name_rep}" in db:
            reply = db[f"{chat_id}_{name_rep}"]
            REPLY = {
                "chat_id": reply.chat_id,
                "name_rep": reply.name_rep,
                "rep": reply.rep,
                "txt_rep": reply.txt_rep,
            }
            return REPLY if REPLY else None


def show_all_reps():
    with shelve.open(Reps_name_file) as db:
        reps = {}
        for key in db:
            reply = db[key]

            print(f"Chat ID: {reply.chat_id}")
            print(f"Name Rep: {reply.name_rep}")
            print(f"rep: {reply.rep}")
            print(f"Txt rep: {reply.txt_rep}")

            print("---")
        return reps


def show_all_reps_grps(chat_id):
    with shelve.open(Reps_name_file) as db:
        reps = {}
        a = 0
        for key, value in db.items():
            if str(value.chat_id) == str(chat_id):
                reps.update(
                    {
                        str(a): {
                            "name": value.name_rep,
                            "reply": value.rep,
                            "txt": value.txt_rep,
                        }
                    }
                )
                a += 1

        return reps


def Delete_reps_by_chat_id(chat_id):
    with shelve.open(Reps_name_file) as db:
        for key in db:
            reply = db[key]
            delete_rep(chat_id, reply.name_rep)


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


def Add_general_response_to_the_bot(name_reply, value_reply):
    with shelve.open(general_response_name_file) as db:
        value_reply = [value_reply]
        if name_reply in db:
            old_value = db[name_reply]
            if not set(value_reply).issubset(set(old_value)):
                db[name_reply] = old_value + value_reply
        else:
            db[name_reply] = value_reply


def Display_generic_response_to_the_bot(name):
    with shelve.open(general_response_name_file) as db:
        if name in db:
            return db[name]
        else:
            return ["None"]


def Del_generic_response_from_the_bot():
    with shelve.open(general_response_name_file) as db:
        for key in db.keys():
            del db[key]


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


class User_privte:
    def __init__(
        self,
        chat_id,
        user_id,
        is_member=None,
        is_blocked=None,
        is_admin=None,
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_member = is_member
        self.is_blocked = is_blocked
        self.is_admin = is_admin


class User_privteDB:
    def __init__(self, db_file):
        self.db = shelve.open(db_file)

    def add_user_private(
        self,
        chat_id,
        user_id,
        is_member=None,
        is_blocked=None,
        is_admin=None,
    ):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]

            if is_blocked is not None:
                user.is_blocked = is_blocked
            if is_member is not None:
                user.is_member = is_member
            if is_admin is not None:
                user.is_admin = is_admin
            user = User_privte(chat_id, user_id, is_member, is_blocked, is_admin)
        else:
            user = User_privte(chat_id, user_id, is_member, is_blocked, is_admin)
        self.db[key] = user

    def update_user_private(
        self,
        chat_id,
        user_id,
        is_member=None,
        is_blocked=None,
        is_admin=None,
    ):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]
            if is_member is not None:
                user.is_member = is_member
            if is_blocked is not None:
                user.is_blocked = is_blocked
            if is_admin is not None:
                user.is_admin = is_admin
            self.db[key] = user

    def delete_user_private(self, chat_id, user_id):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            del self.db[key]

    def delete_users_private(
        self, chat_id, is_member=None, is_blocked=None, is_admin=None
    ):
        Listr = []
        for key in self.db:
            user = self.db[key]
            if user.chat_id == chat_id:
                if is_member:
                    self.add_user(user.chat_id, user.user_id, is_member=False)
                    Listr.append(user.user_id)
                if is_blocked:
                    self.add_user(user.chat_id, user.user_id, is_blocked=False)
                    Listr.append(user.user_id)
                if is_admin:
                    self.add_user(user.chat_id, user.user_id, is_admin=False)
        return Listr

    def display_all_users_privte(self):
        users = {}
        a = 0
        for key in self.db:
            user = self.db[key]
            USER = {
                str(a): {
                    "chat_id": user.chat_id,
                    "user_id": user.user_id,
                    "is_blocked": user.is_blocked,
                    "is_member": user.is_member,
                    "is_admin": user.is_admin,
                }
            }
            a += 1
            # print(USER)
            users.update(USER)
        return users

    def display_user_details_private(self, chat_id, user_id):
        key = f"{chat_id}_{user_id}"
        if key in self.db:
            user = self.db[key]
            USER = {
                "is_blocked": user.is_blocked,
                "is_member": user.is_member,
                "is_admin": user.is_admin,
            }
            return USER
        else:
            return None


def show_admins_bots():
    admis = []
    for user_id in [
        user_id["user_id"]
        for user_id in User_private.display_all_users_privte().values()
        if user_id["is_admin"]
    ]:
        admis.append(user_id)
    return admis


User_private = User_privteDB(User_private_name_file)

print(User_private.display_all_users_privte())
"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""

cr.execute(
    f"create table if not exists 'commands' ('note_inter' text default True, id INTEGER, chanell text default None, Chanell_reply_golbal text default None, message text default '{messagesBots.Compulsory_subscription_letter}', message_join_member text default '{messagesBots.start_message_member},', PRIMARY KEY(id AUTOINCREMENT))"
)


if len(cr.execute("select * from commands").fetchall()) == 0:
    cr.execute(f"insert into 'commands' ('note_inter') values ('True')")


def IdsAdmins():
    IDS = [
        ids["user_id"]
        for ids in User_private.display_all_users_privte().values()
        if ids["is_admin"]
    ]
    return IDS


def update_commnds(Bool):
    cr.execute(f"update 'commands' set note_inter = '{Bool}'")
    db.commit()


def IsBool():
    data = cr.execute("select note_inter from commands ").fetchone()[0]
    return True if data == "True" else False


def update_chanell(chanell):
    cr.execute(f"update 'commands' set chanell = '{chanell}'")
    db.commit()


def update_Chanell_reply_golbal(chanell):
    cr.execute(f"update 'commands' set Chanell_reply_golbal = '{chanell}'")
    db.commit()


def Ischannell():
    data = cr.execute("select chanell from commands ").fetchone()[0]
    return data


def IsChanell_reply_golbal():
    data = cr.execute("select Chanell_reply_golbal from commands ").fetchone()[0]
    return data


def deleteChanell():
    cr.execute(f"update 'commands' set chanell = 'None'")
    db.commit()


def deleteChanell_reply_golbal():
    cr.execute(f"update 'commands' set Chanell_reply_golbal = 'None'")
    db.commit()


def update_message(message):
    cr.execute(f"update 'commands' set message = '{message}'")
    db.commit()


def Ismessage():
    data = cr.execute("select message from commands ").fetchone()[0]
    return data


def update_message_join_member(chanell):
    cr.execute(f"update 'commands' set message_join_member = '{chanell}'")
    db.commit()


def Ismessage_join_member():
    data = cr.execute("select message_join_member from commands ").fetchone()[0]
    return str(data)


def deleteMessage_join_member():
    cr.execute(
        f"update 'commands' set message_join_member = '{messagesBots.start_message_member}'"
    )
    db.commit()


def check_user(user_id):
    ISMember = User_private.display_user_details_private(IsDevloper(), user_id)
    if ISMember is not None and ISMember["is_member"]:
        return False
    else:
        return True


def check_muted(user_id):
    ISMuted = User_private.display_user_details_private(IsDevloper(), user_id)
    if ISMuted is not None and ISMuted["is_blocked"]:
        return False
    else:
        return True


"""








SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS








"""


Ranks = [
    "member",
    "distinct",
    "muted",
    "admin",
    "blocked",
    "banned",
    "reeve",
    "cretor",
    "devloper",
    "cretor2",
    "devloper2",
    "owner",
    "owner2",
    "owner2",
    "bulder",
    "dev",
]


def promotions_function(message: Message, Rank_name, my_id):
    user_1 = message.from_user
    user_2 = message.reply_to_message.from_user
    chat_id = message.chat.id
    Get_Rank_1 = show_user_info(chat_id, user_1.id)["rank"]
    Get_Rank_2 = show_user_info(chat_id, user_2.id)["rank"]

    def Is_acceptable(typ):
        if (
            IsDevloper() == user_1.id
            or Get_Rank_1 == "bulder"
            or Get_Rank_1 == "programmer"
        ):
            return True
        else:
            if typ == 1:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                ]
            if typ == 2:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]
            if typ == 3:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creator2",
                ]
            if typ == 4:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creator2",
                    "creator",
                ]
            if typ == 5:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creator2",
                    "creator",
                    "owner2",
                ]
            if typ == 6:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creator2",
                    "creator",
                    "owner2",
                    "owner",
                ]
            if typ == 7:
                return Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creator2",
                    "creator",
                    "owner2",
                    "owner",
                    "devloper2",
                ]

            if typ == 8:
                return Get_Rank_1 == "bulder"

    if Rank_name == "distinct":
        if Is_acceptable(typ=1):
            if Get_Rank_2 == "member":
                update_user(chat_id, user_2.id, rank_user="distinct")
            return "تم رفعة ميمز"
        else:
            return "هذا الامر يخص المدراء"
    if Rank_name == "admin":
        if Is_acceptable(typ=1):
            if Get_Rank_2 in ["member", "distinct"]:
                update_user(chat_id, user_2.id, rank_user="admin")
            return "تم رفعة ادمن"
        else:
            return "هذا الامر يخص المدراء فقط"

    if Rank_name == "reeve":
        if Is_acceptable(typ=2):
            if Get_Rank_2 in ["member", "distinct", "admin"]:
                update_user(chat_id, user_2.id, rank_user="reeve")
            return "تم رفعه مدير"
        else:
            return "هذا الامر يخص المنشئين الثانويين"

    if Rank_name == "creator2":
        if Is_acceptable(typ=3):
            if Get_Rank_2 in ["member", "distinct", "admin", "reeve"]:
                update_user(chat_id, user_2.id, rank_user="creator2")
            return "تم رفعة منشئ ثانوي"
        else:
            return "هذا الامر يخص المنشئين"

    if Rank_name == "creator":
        if Is_acceptable(typ=4):
            if Get_Rank_2 in ["member", "distinct", "admin", "reeve", "creator2"]:
                update_user(chat_id, user_2.id, rank_user="creator")
            return "تم رفعة منشئ"
        else:
            return "هذا الامر يخص  المالكين الثانويين"

    if Rank_name == "owner2":
        if Is_acceptable(typ=5):
            if Get_Rank_2 in [
                "member",
                "distinct",
                "admin",
                "reeve",
                "creator2",
                "creator",
            ]:
                update_user(chat_id, user_2.id, rank_user="owner2")
            return "تم رفعة مالك ثانوي"
        else:
            return "هذا الامر يخص المالكين"

    if Rank_name == "owner":
        if Is_acceptable(typ=6):
            if Get_Rank_2 in [
                "member",
                "distinct",
                "admin",
                "reeve",
                "creator2",
                "creator",
                "owner2",
            ]:
                update_user(chat_id, user_2.id, rank_user="owner")
            return "تم رفعة مالك"
        else:
            return "هذا الامر يخص مالك المجموعة او المطور"

    if Rank_name == "devloper2":
        if Is_acceptable(typ=6):
            if Get_Rank_2 in [
                "member",
                "distinct",
                "admin",
                "reeve",
                "creator2",
                "creator",
                "owner2",
                "owner",
            ]:
                update_user(chat_id, user_2.id, rank_user="devloper2")
            return "تم رفعة مطور ثانوي"
        else:
            return "هذا الامر يخص مالك المجموعة او المطور"

    if Rank_name == "devloper":
        if Is_acceptable(typ=6):
            if Get_Rank_2 in [
                "member",
                "distinct",
                "admin",
                "reeve",
                "creator2",
                "creator",
                "owner2",
                "owner",
                "devloper2",
            ]:
                update_user(chat_id, user_2.id, rank_user="devloper")
            return "تم رفعة مطور"
        else:
            return "هذا الامر يخص مالك المجموعة او المطور"


def download_function(message: Message, Rank_name, my_id):
    user_1 = message.from_user
    user_2 = message.reply_to_message.from_user
    chat_id = message.chat.id
    Get_Rank_1 = show_user_info(chat_id, user_1.id)["rank"]
    Get_Rank_2 = show_user_info(chat_id, user_2.id)["rank"]

    def Is_acceptable(typ):
        if typ == 1:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله مميز"]
            else:
                if Get_Rank_2 in ["member", "distinct", "admin"] and Get_Rank_2 not in [
                    "member",
                    "distinct",
                    "admin",
                    "muted",
                    "blocked",
                    "banned",
                ]:
                    return ["True", "تم تنزيله مميز"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return ["True", "تم تنزيله مميز"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return ["True", "تم تنزيله مميز"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return ["True", "تم تنزيله مميز"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله مميز"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله مميز"]

                if Get_Rank_2 in ["member", "distinct", "admin"] and Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "muted",
                    "blocked",
                    "banned",
                ]:
                    return "هذا الامر للمدراء فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return "هذا الامر يخص المنشئين الثانويين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return "هذا الامر يخص المنشئين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return "هذا الامر يخص المالكين الثانويين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

        if typ == 2:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله ادمن"]
            else:
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return ["True", "تم تنزيله ادمن"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return ["True", "تم تنزيله ادمن"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return ["True", "تم تنزيله ادمن"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله ادمن"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله ادمن"]

                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return "هذا الامر يخص المنشئين الثانويين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return "هذا الامر يخص المنشئين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return "هذا الامر يخص المالكين الثانويين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

        if typ == 3:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله مدير"]
            else:
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return ["True", "تم تنزيله مدير"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return ["True", "تم تنزيله مدير"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله مدير"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله مدير"]

                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return "هذا الامر يخص المنشئين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return "هذا الامر يخص المالكين الثانويين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

        if typ == 4:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله منشئ ثانوي"]
            else:
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return ["True", "تم تنزيله منشئ ثانوي"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله منشئ ثانوي"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله منشئ ثانوي"]

                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return "هذا الامر يخص المالكين الثانويين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

        if typ == 5:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله منشئ"]
            else:
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله منشئ"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله منشئ"]

                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

        if typ == 6:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله مطور ثانوي"]
            else:
                return "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"

        if typ == 7:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله مطور"]
            else:
                return "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"

        if typ == 8:
            if (
                user_1.id == IsDevloper()
                or Get_Rank_1 == "bulder"
                or Get_Rank_1 == "programmer"
            ):
                return ["True", "تم تنزيله من كل الرتب"]
            else:
                if Get_Rank_2 in ["member", "distinct", "admin"] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "muted",
                    "blocked",
                    "banned",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ]:
                    return ["True", "تم تنزيله من كل الرتب"]

                if Get_Rank_2 in ["member", "distinct", "admin"] and Get_Rank_1 in [
                    "member",
                    "distinct",
                    "admin",
                    "muted",
                    "blocked",
                    "banned",
                ]:
                    return "هذا الامر للمدراء فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                ]:
                    return "هذا الامر يخص المنشئين الثانويين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                ]:
                    return "هذا الامر يخص المنشئين"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                ]:
                    return "هذا الامر يخص المالكين الثانويين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                ]:
                    return "هذا الامر يخص المالكين فقط"
                if Get_Rank_2 in [
                    "member",
                    "distinct",
                    "admin",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                ] and Get_Rank_1 not in [
                    "member",
                    "distinct",
                    "admin",
                    "blocked",
                    "muted",
                    "banned",
                    "reeve",
                    "creaator2",
                    "creaator",
                    "owner2",
                    "owner",
                    "devloper",
                    "devloper2",
                ]:
                    return (
                        "هذا الامر يخص المطور الاصلي او مالك المجموعه او المطورين فقط"
                    )

    if Rank_name == "distinct":
        if "True" in Is_acceptable(typ=1):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=1)[1]
        else:
            return Is_acceptable(typ=1)

    if Rank_name == "admin":
        if "True" in Is_acceptable(typ=2):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=2)[1]
        else:
            return Is_acceptable(typ=2)

    if Rank_name == "reeve":
        if "True" in Is_acceptable(typ=3):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=3)[1]
        else:
            return Is_acceptable(typ=3)

    if Rank_name == "creator2":
        if "True" in Is_acceptable(typ=4):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=4)[1]
        else:
            return Is_acceptable(typ=4)

    if Rank_name == "creator":
        if "True" in Is_acceptable(typ=5):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=5)[1]
        else:
            return Is_acceptable(typ=5)

    if Rank_name == "owner2":
        if "True" in Is_acceptable(typ=6):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=6)[1]
        else:
            return Is_acceptable(typ=6)

    if Rank_name == "devloper2":
        if "True" in Is_acceptable(typ=6):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=6)[1]
        else:
            return Is_acceptable(typ=6)

    if Rank_name == "devloper":
        if "True" in Is_acceptable(typ=7):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=7)[1]
        else:
            return Is_acceptable(typ=7)

    if Rank_name == "tk":
        if "True" in Is_acceptable(typ=8):
            update_user(chat_id, user_2.id, rank_user="member")
            return Is_acceptable(typ=8)[1]
        else:
            return Is_acceptable(typ=8)


def mute_function_van(message: Message, my_id):
    ch = message.chat.id
    ad = message.from_user
    us = message.reply_to_message.from_user
    Get_Rank_1 = show_user_info(ch, ad.id)["rank"]
    Get_Rank_2 = show_user_info(ch, us.id)["rank"]

    if Get_Rank_1 in ["member", "distinct", "admin", "muted", "blocked", "banned"]:
        return "هذا الامر مخصص للمدراء فما فوق"

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 in ["member"]:
            return ["True", "تم كتمه"]

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 not in ["member"]:
            return "لا يمكن كتم المميزين"


def ban_function_van(message: Message, my_id):
    ch = message.chat.id
    ad = message.from_user
    us = message.reply_to_message.from_user
    Get_Rank_1 = show_user_info(ch, ad.id)["rank"]
    Get_Rank_2 = show_user_info(ch, us.id)["rank"]
    if Get_Rank_1 in ["member", "distinct", "admin", "muted", "blocked", "banned"]:
        return "هذا الامر مخصص للمدراء فما فوق"

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 in ["member"]:
            return ["True", "تم طرده"]

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 not in ["member"]:
            return "لا يمكن طرد المميزين"


def block_function_van(message: Message, my_id):
    ch = message.chat.id
    ad = message.from_user
    us = message.reply_to_message.from_user
    Get_Rank_1 = show_user_info(ch, ad.id)["rank"]
    Get_Rank_2 = show_user_info(ch, us.id)["rank"]
    if Get_Rank_1 in ["member", "distinct", "admin", "muted", "blocked", "banned"]:
        return "هذا الامر مخصص للمدراء فما فوق"

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 in ["member"]:
            return ["True", "تم حظره"]

    if (
        Get_Rank_1 not in ["member", "distinct", "admin", "muted", "blocked", "banned"]
        or IsDevloper() == us.id
        or Get_Rank_1 == "bulder"
        or Get_Rank_1 == "programmer"
    ):
        if Get_Rank_2 not in ["member"]:
            return "لا يمكن حظر المميزين"


def unmute_function_van(message: Message, my_id):
    ch = message.chat.id
    ad = message.from_user
    us = message.reply_to_message.from_user
    Get_Rank_1 = show_user_info(ch, ad.id)["rank"]
    Get_Rank_2 = show_user_info(ch, us.id)["rank"]
    if IsDevloper() == us.id or Get_Rank_1 == "bulder" or Get_Rank_1 == "programmer":
        return ["True", "تم الغاء كتمه"]

    elif Get_Rank_1 in ["member", "distinct", "admin", "muted", "blocked", "banned"]:
        return "هذا الامر مخصص للمدراء فما فوق"

    elif Get_Rank_1 not in [
        "member",
        "distinct",
        "admin",
        "muted",
        "blocked",
        "banned",
    ]:
        return ["True", "تم الغاء كتمه"]


def unblock_function_van(message: Message, my_id):
    ch = message.chat.id
    ad = message.from_user
    us = message.reply_to_message.from_user
    Get_Rank_1 = show_user_info(ch, ad.id)["rank"]
    Get_Rank_2 = show_user_info(ch, us.id)["rank"]
    if IsDevloper() == us.id or Get_Rank_1 == "bulder" or Get_Rank_1 == "programmer":
        return ["True", "تم الغاء حظره"]

    elif Get_Rank_1 in ["member", "distinct", "admin", "muted", "blocked", "banned"]:
        return "هذا الامر مخصص للمدراء فما فوق"

    elif Get_Rank_1 not in [
        "member",
        "distinct",
        "admin",
        "muted",
        "blocked",
        "banned",
    ]:
        return ["True", "تم الغاء حظره"]


def Add_general_response_to_the_bot(name_reply, value_reply):
    with shelve.open(general_response) as db:
        value_reply = [value_reply]
        if name_reply in db:
            old_value = db[name_reply]
            if not set(value_reply).issubset(set(old_value)):
                db[name_reply] = old_value + value_reply
        else:
            db[name_reply] = value_reply


def Add_general_response_to_the_bot(name_reply, value_reply):
    with shelve.open(general_response) as db:
        value_reply = [value_reply]
        if name_reply in db:
            old_value = db[name_reply]
            if not set(value_reply).issubset(set(old_value)):
                db[name_reply] = old_value + value_reply
        else:
            db[name_reply] = value_reply


def Del_general_response_fromBOT(name_replyy):
    with shelve.open(general_response) as db:
        if name_replyy in db:
            del db[name_replyy]


def DelAll_general_response_from_the_bot():
    with shelve.open(general_response) as db:
        for key in db.keys():
            try:
                del db[key]
            except:
                pass


def Display_generic_response_to_the_bot(name):
    with shelve.open(general_response) as db:
        if name in db:
            return db[name]
        else:
            return ["None"]


def showGloblaReply(name):
    reps = Display_generic_response_to_the_bot(name)
    if reps != ["None"]:
        return random.choice(reps)
    else:
        return False

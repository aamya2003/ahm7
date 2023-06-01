import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *


def Member_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) == "member":
        return True
    else:
        return False


def Distinct_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) != "member":
        return True
    else:
        return False


def Admin_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in ["member", "distinct"]:
        return True
    else:
        return False


def Reave_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in ["member", "distinct", "admin"]:
        return True
    else:
        return False


def Creator2_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in ["member", "distinct", "admin", "reeve"]:
        return True
    else:
        return False


def Creator_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in [
        "member",
        "distinct",
        "admin",
        "reeve",
        "creator2",
    ]:
        return True
    else:
        return False


def Owner2_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in [
        "member",
        "distinct",
        "admin",
        "reeve",
        "creator2",
        "creator",
    ]:
        return True
    else:
        return False


def Owner_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in [
        "member",
        "distinct",
        "admin",
        "reeve",
        "creator2",
        "creator",
        "owner2",
    ]:
        return True
    else:
        return False


def Devloper2_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in [
        "member",
        "distinct",
        "admin",
        "reeve",
        "creator2",
        "creator",
        "owner2",
        "owner",
    ]:
        return True
    else:
        return False


def Devloper_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) not in [
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
        return True
    else:
        return False


def Bulder_user(chat_id, user_id):
    if Get_rank_user(chat_id, user_id) == "bulder":
        return True
    else:
        return False


def Programer_user(user_id):
    if IsDevloper() == user_id or user_id in show_admins_bots():
        return True
    else:
        return False

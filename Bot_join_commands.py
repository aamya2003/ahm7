import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *



def Bot_join(message: ChatMemberUpdated):
  chID = message.chat.id
  ADMIN = message.from_user
  old = message.old_chat_member
  new = message.new_chat_member

  if (new.status == "member" or 'admin' in new.status):
    
    info = bot.get_chat_member(message.chat.id, ADMIN.id)

    # is admin or crator or dev or not
    if info.status == "creator" or info.status == "administrator" or ADMIN.id == My_id:
      # is group in database or not
      if not check_group(message.chat.id):
        # is bot has all premations or not
        if all_pre(bot, message.chat.id):
          insert_group(message.chat.id)
          bot.send_message(chat_id=chID,text=f"-- تم تفعيل البوت في المجموعه \n -- تم التفعيل بواسطه: {ADMIN.first_name}",parse_mode="HTML")
          Automatic_lift(message.chat.id)
        else:
          bot.send_message(chat_id=message.chat.id, text="عذرا, يجب اعطائي كافه الصلاحيات !",parse_mode="HTML")
      else:
        bot.send_message(chat_id=message.chat.id, text=f"⌔︙ تم تفعيلها مسبقا",parse_mode="HTML")
    else:
      bot.send_message(chat_id=message.chat.id, text="هذا الامر مخصص للمشرفين فقط" ,parse_mode="HTML")
  if 'admin' in old.status and new.status in ['member', 'left', 'kicked']:
    delete_group(message.chat.id)
    Delete_users_by_chat_id(message.chat.id)


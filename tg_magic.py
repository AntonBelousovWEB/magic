import pyowm
import time
import sys
from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import pyowm

print('''
██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███████╗██████╗░░██████╗  ░░░░░░
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝  ░░░░░░
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝█████╗░░██████╔╝╚█████╗░  █████╗
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██╔══╝░░██╔══██╗░╚═══██╗  ╚════╝
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░███████╗██║░░██║██████╔╝  ░░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░  ░░░░░░

██╗██╗░█████╗░██╗░░██╗██╗██╗██╗
╚█║╚█║██╔══██╗██║░██╔╝██║╚█║╚█║
░╚╝░╚╝██║░░██║█████═╝░██║░╚╝░╚╝
░░░░░░██║░░██║██╔═██╗░╚═╝░░░░░░
░░░░░░╚█████╔╝██║░╚██╗██╗░░░░░░
░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░''')
# print('Данная программа не нисет в себе ничего плохого и мы не заставляем использывать в плохих целях, с уважением разработчики - "Ok!"')
# t = input("Введите пароль от скрипта:")
# if t!="settings1":
#         print('Неправильный пароль')
#         print(''' 
#                   ████   ████
#                   ████   ████
          
#                   ███████████
#                  █           █''')
#         time.sleep(2)
#         sys.exit()
# else:
#         print('Привет хозяин ')
#         print('''
#                 ▄▄▄▄▄
#           ▄▄█████████████▄▄▄
#         ██████▀▀▀▀░░▀▀▀███████
#        ███░░░░░░░░░░░░░░░░░▀███
#       ███░░░░░░░░░░░░░░░░░░░░██
#     ████░░░░░██░░░░░░░██░░░░░▐███
#     ████░░░░░░░░░░█░░░░░░░░░░▐███
#     ███▌░░░░░░░░░░░░░░░░░░░░░▐███
#       ██░░░░░░░░█░░░░█░░░░░░░▐█
#       ▐██░░░░░░░░████░░░░░░░░██
#        ███░░░░░░░░░█░░░░░░░░███
#         ███▄░░░░░░░░░░░░░░▄███
#          █████▄▄░░░░░░░▄█████
#            ▀██████████████▀
# ''')
#         time.sleep(1)

bot = Client('antosha-session', 8449169, "20b6754029252ed4fa6c8fcdd465d9d7")
bot.start()

bot.stop()

print('Бот запущен, теперь ты - "Адский Спамер"')
print('Команды: magic||♥ magic||Magic||♥ Magic.')
print('''P.S. - (Скрипт был разработан при поддержке программистов - "Ok!"
         Наш Discord: https://discord.gg/mxKZtFtMwp)''')

@bot.on_message(filters.regex('magic|♥ magic|Magic|♥ Magic') & filters.me)
def ghoul_spam_handler(client, message):
    bot.send_message(message.chat.id, """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    time.sleep(1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍♥♥🤍♥♥🤍🤍
🤍♥♥♥♥♥♥♥🤍
🤍♥♥♥♥♥♥♥🤍
🤍♥♥♥♥♥♥♥🤍
🤍🤍♥♥♥♥♥🤍🤍
🤍🤍🤍♥♥♥🤍🤍🤍
🤍🤍🤍🤍♥🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💛💛🤍🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍🤍💛💛💛💛💛🤍🤍
🤍🤍🤍💛💛💛🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💚💚🤍💚💚🤍🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💚💚💚💚💚🤍🤍
🤍🤍🤍💚💚💚🤍🤍🤍
🤍🤍🤍🤍💚🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤎🤎🤍🤎🤎🤍🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤍🤎🤎🤎🤎🤎🤍🤍
🤍🤍🤍🤎🤎🤎🤍🤍🤍
🤍🤍🤍🤍🤎🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🧡🤍🧡🧡🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🤍🧡🧡🧡🧡🧡🤍🤍
🤍🤍🤍🧡🧡🧡🤍🤍🤍
🤍🤍🤍🤍🧡🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💚🤍🧡♥🤍🤍
🤍💚🖤💛🧡💙🖤💙🤍
🤍♥💙🖤🧡💙🤎🖤🤍
🤍🤎🖤♥💛🧡💙💛🤍
🤍🤍💛💙🖤🧡🤎🤍🤍
🤍🤍🤍🧡🤍🖤🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤💛🤍🧡🤎🤍🤍
🤍🤍♥💛🤎🖤💙💛🤍
🤍🖤🤍🧡💚🖤💚💙🤍
🤍💛🖤💙💚💙🖤🤍🤍
🤍🤍💚🧡🤍💚💛🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍🧡🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍💙🤎💙💙💙🖤💙🤍
🤍💙💙💙🧡💙💙💙🤍
🤍💙💛💙💙💙💙🧡🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙🤎🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍🖤💙💙💙💙♥💙🤍
🤍💙💙💙💙💛💙💙🤍
🤍💙🤍💙💙💙💙💙🤍
🤍🤍💙💙🤎💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""🤍🤍🤍🤍🤍🤍🤍🤍🤍
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙
💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""💙""")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id + 1, text="""developed by @Yaitismylife""")

bot.run()
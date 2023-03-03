from utils import decorator
from config import log_channel 
from errors.log import log
from telegram.constants import ParseMode

@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    bot = context.bot
    try:
        await bot.ban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)
        await update.message.reply_text(text="<b>Ban process</b>\n\n"
                                             "User_id: <code>{}</code>\n"
                                             "Name: {}\n"
                                             "Username: @{}\n\n"
                                             "Succesfully banned".format(update.message.reply_to_message.from_user.id,
                                                                             update.message.reply_to_message.from_user.first_name,
                                                                             update.message.reply_to_message.from_user.username),
                                        parse_mode=ParseMode.HTML)
        await context.bot.delete_message(update.message.chat_id, update.message.message_id)

        # resoconto gruppo admin
        text = context.args
        mess = ''
        for txt in text:
            mess = mess + ' ' + txt
        if mess == '':
            mess = 'not provided'
        await context.bot.send_message(chat_id=log_channel , text="🔴 <b>Ban process</b> #ban\n\n"
                                                                  "Chat: {}\n"
                                                                  "Chat_id: {}\n"
                                                                  "User_id: <code>{}</code>\n"
                                                                  "Name: {}\n"
                                                                  "Username: @{}\n\n"
                                                                  "<b>Performed by admin</b>: @{}\n\n"
                                                                  "<b>Ban reason</b>: {}".format(update.message.chat.title,
                                                                                                 update.message.chat_id,
                                                                                                 update.message.reply_to_message.from_user.id,
                                                                                                 update.message.reply_to_message.from_user.first_name,
                                                                                                 update.message.reply_to_message.from_user.username,
                                                                                                 update.message.from_user.username,
                                                                                                 mess),
                                       parse_mode=ParseMode.HTML)

    except:
        log("an error occurred [BAN] function")
        await update.message.reply_text("Error during ban operation")

import os
import random
import html

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from config import OWNER_ID



async def send_groups_document(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in OWNER_ID:
        update.message.reply_text('Only For owner...')
        return
    cursor = top_global_groups_collection.find({})
    groups = []
    async for document in cursor:
        groups.append(document)
    group_list = ""
    for group in groups:
        group_list += f"{group['group_name']}\n"
        group_list += "\n"
    with open('groups.txt', 'w') as f:
        f.write(group_list)
    with open('groups.txt', 'rb') as f:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=f)
    os.remove('groups.txt')


application.add_handler(CommandHandler('groups', send_groups_document, block=False))

from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto

@app.on_message(filters.command(["tgm", "telegraph"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = await message.reply("⏳")
        path = await reply.download()  # Download media file
        try:
            # Upload the file to Telegraph
            result = upload_file(path)
            url = "https://telegra.ph" + result[0]
            await i.edit(f'ᴜʀ ʟɪɴᴋ: {url}')
        except Exception as e:
            await i.edit(f"Error: {e}")

###

@app.on_message(filters.command(["graph", "grf"]))
async def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = await message.reply("⏳")
        path = await reply.download()  # Download media file
        try:
            # Upload the file to Graph.org
            result = upload_file(path)
            url = "https://graph.org" + result[0]
            await i.edit(f'ᴜʀ ʟɪɴᴋ: {url}')
        except Exception as e:
            await i.edit(f"Error: {e}")


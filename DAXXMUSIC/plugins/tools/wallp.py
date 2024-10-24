from requests import get 
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from DAXXMUSIC import app as app


@app.on_message(filters.command("wallpapers"))
async def pinterest(_, message):
    chat_id = message.chat.id
    try:
        query= message.text.split(None,1)[1]
    except:
        return await message.reply("Input image name for search 🔍")

    msg = await message.reply("🔍")
    
    images = get(f"https://hoshi-api-f62i.onrender.com/api/wallpaper?query={query}").json()
    media_group = []
    count = 0

    for url in images["images"][:8]:

        media_group.append(InputMediaPhoto(media=url))
        count += 1
    
    await msg.edit(f"=> ✅ Fetched {count} wallpapers...")
    try:
        
        await bot.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"Error\n{e}")

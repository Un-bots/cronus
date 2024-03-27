from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
⚠️Sᴏʀʀʏ, ʙᴜᴛ ᴛʜᴇ 神 𝗞ɪʀᴀ's ʀᴇᴘᴏ ɪs ɴᴏᴛ ᴘᴜʙʟɪᴄ. 

✰ Iғ ʏᴏᴜ ᴡᴀɴᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴀsᴋ ᴅᴇᴠ
 
► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss

✰ Tʜᴀɴᴋ ʏᴏᴜ🧡
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/un_bots"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/LU6I3R"),
        ],
        [
         InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗚𝗥𝗢𝗨𝗣", url="https://t.me/+qzwE0S3s6ps5YzVl"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/2945b87231919e729afb9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/un-bots/shadow/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/un-bots/shadow) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/UN_W0RLD)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")



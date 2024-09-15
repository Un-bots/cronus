import time
import aiohttp
from DAXXMUSIC import app
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

# Command handler for ChatGPT
@app.on_message(filters.command(["chatgpt", "ai", "ask", "gpt", "solve"], prefixes=["+", ".", "/", "-", "!", "$", "#", "&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Check if there is a question after the command
        if len(message.command) < 2:
            await message.reply_text("Example:\n\n/chatgpt Where is TajMahal?")
        else:
            question = message.text.split(' ', 1)[1]
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://chatgpt.apinepdev.workers.dev/?question={question}') as response:
                    if response.status == 200:
                        json_response = await response.json()
                        if "answer" in json_response:
                            answer = json_response["answer"]
                            end_time = time.time()
                            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                            await message.reply_text(
                                f"{answer}\n\nᴀɴsᴡᴇʀɪɴɢ ʙʏ ➛ @kira_probot\nResponse Time: {telegram_ping}",
                                parse_mode=ParseMode.MARKDOWN
                            )
                        else:
                            await message.reply_text("No 'answer' key found in the response.")
                    else:
                        await message.reply_text("Failed to get a valid response from the server.")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")

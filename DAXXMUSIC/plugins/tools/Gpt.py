import time
import aiohttp
import openai
from DAXXMUSIC import app
from config import BOT_USERNAME

from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

# Set your OpenAI API key
openai.api_key = "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"

@app.on_message(filters.command(["chatgpt", "ai", "ask", "gpt", "solve"], prefixes=["+", ".", "/", "-", "!", "$", "#", "&"]))
async def chat_gpt(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text("Example:\n\n/chatgpt Where is TajMahal?")
        else:
            question = message.text.split(' ', 1)[1]
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",  # You can use different models as needed
                    prompt=question,
                    max_tokens=150
                )
                answer = response.choices[0].text.strip()
                end_time = time.time()
                telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
                await message.reply_text(
                    f"{answer}\n\nᴀɴsᴡᴇʀɪɴɢ ʙʏ ➛ @kira_probot\nResponse Time: {telegram_ping}",
                    parse_mode=ParseMode.MARKDOWN
                )
            except Exception as e:
                await message.reply_text(f"Error with OpenAI API: {str(e)}")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")

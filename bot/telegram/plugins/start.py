from bot.helper.media import is_media
from bot.telegram import StreamBot
from pyrogram import filters, Client
from pyrogram.types import Message

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(bot: Client, message: Message):
    if "file_" in message.text:
        try:
            usr_cmd = message.text.split("_")[-1]
            data = usr_cmd.split("-")
            message_id, chat_id = int(data[0]), int(data[1])
            file = await bot.get_messages(chat_id, message_id)
            media = is_media(file)
            await message.reply_cached_media(file_id=media.file_id, caption=f'**{media.file_name}**', disable_notification=True)
        except Exception as e:
            print(f"An error occurred: {e}")

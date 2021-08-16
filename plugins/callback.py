import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start, BATCH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """**You need Help?? 🧐**

★ Just send me the files i will store file and give you share able link


**You can use me in channel too 😉**

★ Make me admin in your channel with edit permission. Thats enough now continue uploading files in channel i will edit all posts and add share able link url buttons

**How to enable uploader details in caption**

★ Use /mode command to change and also you can use `/mode channel_id` to control caption for channel msg."""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏕', callback_data='home'),
            InlineKeyboardButton('About 📕', callback_data='about')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
    about_text = f"""--**My Details:**--

👋 𝐌𝐲 𝐍𝐚𝐦𝐞: {bot.mention(style='md')}

🤖 Main Robot: [Entertainment Bot](https://t.me/FunyRobot)
    
❤️ Main Channel: [Multi Audio Films/Movies/Series](https://t.me/MultiAudioFilms)

♻️ Index Channel: [Film Index](https://t.me/FilmIndex)

💎 Our Group : [Our Group Chat](https://t.me/OurGroupChat)

🔥 Hindi Movies : [Hindi Movies](https://t.me/Hindi_Telegram)

🐾 Anime Channel: [Popular Anime](https://t.me/PopularAnime)

📢 Backup Channel: [Dual Audio Army Backup](https://t.me/DualAudioArmyBkp) 

⚡ Share: [Share With Friends](https://telegram.me/share/url?url=https%3A%2F%2Ft.me%2FFunyRobot%0D%0Ahttps%3A%2F%2Ft.me%2FFilmIndex+%0D%0Ahttps%3A%2F%2Ft.me%2FMultiAudioFilms++%0D%0Ahttps%3A%2F%2Ft.me%2FHindiHindi_Movie++++%0D%0Ahttps%3A%2F%2Ft.me%2FPopularAnime+%0D%0Ahttps%3A%2F%2Ft.me%2FDualAudioArmyBkp++%0D%0Ahttps%3A%2F%2Ft.me%2FIndianFunnyVideos++%0D%0Ahttps%3A%2F%2Ft.me%2FOnlineFunnyArmy+%0D%0Ahttps%3A%2F%2Ft.me%2FHindi_Telegram%0D%0Ahttps%3A%2F%2Ft.me%2FAd_ibot++%0D%0A....+and+more+on+%40FunyRobot+%F0%9F%A4%96++%0D%0A++%0D%0A%F0%9F%91%86%F0%9F%91%86Follow+the+above+link+to+DOWNLOAD+All+HOLLYWOOD%2C+ANIME%2C+BOLLYWOOD%2C+TOLLYWOOD%2C+PREMIUM+MOVIES+%26+SERIES+in+MULTI+AUDIO+with+BEST+QUALITY+%F0%9F%A5%B0++++%0D%0A++++%0D%0A%F0%9F%A6%8B+BECOME+A+PART+OF+OUR+GROWING+FAMILY+%F0%9F%8C%B8) 
"""

    # creating buttons
    buttons = [
        [
            InlineKeyboardButton('Home 🏕', callback_data='home'),
            InlineKeyboardButton('Help 💡', callback_data='help')
        ],
        [
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]
    ]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)


@Client.on_callback_query(filters.regex('^done$'))
async def done_cb(c, m):
    BATCH.remove(m.from_user.id)
    c.cancel_listener(m.from_user.id)
    await m.message.delete()


@Client.on_callback_query(filters.regex('^delete'))
async def delete_cb(c, m):
    await m.answer()
    cmd, msg_id = m.data.split("+")
    chat_id = m.from_user.id if not DB_CHANNEL_ID else int(DB_CHANNEL_ID)
    message = await c.get_messages(chat_id, int(msg_id))
    await message.delete()
    await m.message.edit("Deleted files successfully 👨‍✈️")

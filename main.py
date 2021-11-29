from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

import requests 

import os


API = "https://apis.xditya.me/lyrics?song="


rizad = Client(
    "Lyrics-Finder-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@rizad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hy {} \n\n**I'm Lyrics Finder Bot. Send Me A Song Name, I Will Give You The Lyrics. ** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Developer 🎀", url = "https://telegram.me/riz4d"),InlineKeyboardButton("Instagram", url = "https://instagram.com/rizad__x96")],[InlineKeyboardButton("Github", url = "https://github.com/riz4d/Lyrics-Finder-Bot")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@rizad.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    ABOUT = "**Lyrics Bot :** Lyrics Search Bot\n\n**🧑‍💻 Developer :** [rizad](https://github.com/riz4d)\n\n**🛡️ Framework :** Pyrogram"
    await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)

@rizad.on_message(filters.private & filters.text)
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song) 
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev 🔗 ", url = f"github.com/riz4d")]]))
        except requests.ConnectionError as exception:
        	await hy.delete()
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = f"github.com/riz4d")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Extracted by @riz4d**'
        return text


rizad.run()

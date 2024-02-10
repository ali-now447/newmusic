#telegram: @lllby ~ My channel: @mmmsc .
import os
import random
import asyncio
from pyrogram import Client,filters
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from ZelzalMusic import app

@app.on_message(command("سوس") & filters.group)
async def bottttt(client, message):
    selections = [f"هَلا فيك . {message.from_user.mention}", 
f"يحبك . {message.from_user.mention}",
f" عُيونه . {message.from_user.mention}",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    

@app.on_message(command([f"غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,122)
    url = f"https://t.me/EmmaBotVoice/{rl}"
    await client.send_voice(message.chat.id,url,caption=f"🧚🏼‍♂️ ¦ تم أختياࢪ أغنية لك {message.from_user.mention}",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/mmmsc")
                ],
            ]
        )
    )
@app.on_message(
    command(["المطور"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("z_o_i")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"≭︰Information Devloper ↯.\n\n━─━─────━─────━─━\n\n≭︰Name ↬ ❲{name}❳\n≭︰Bio ↬{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

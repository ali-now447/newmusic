from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app
@app.on_message(
    command(["المطور"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("lllby")
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

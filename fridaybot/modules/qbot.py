# port to DARK COBRA by @hellboi-atul

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot import bot

from ..utils import admin_cmd


@borg.on(admin_cmd(pattern=r"qubot(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()

    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Making a Quote```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await event.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)

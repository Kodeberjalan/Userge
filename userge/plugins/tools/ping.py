# Copyright (C) 2020-2021 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.
import requests

from datetime import datetime

from userge import userge, Message


@userge.on_cmd("ping", about={
    'header': "check how long it takes to ping your userbot",
    'flags': {'-t': "ping telegram dc following user dc"}}, group=-1)
async def pingme(message: Message):
    start = datetime.now()
    me_dc = (await message.client.get_me()).dc_id
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    tg_url = f"https://cdn{me_dc}.telesco.pe"
    ping = round(requests.head(tg_url).elapsed.total_seconds() * 1000)
    await message.edit('`Pong!`')
    if '-t' in message.flags:
    	await message.edit(f"**Pong!**\n`{ping} ms`")
    else:
    	await message.edit(f"**Pong!**\n`{m_s} ms`")
    
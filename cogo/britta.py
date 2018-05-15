#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The Britta Bot will be in charge of greeting new members, and role
assignment
Will be started by the controller"""


import sys
import os
MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MY_PATH + '/../')

import cogo.controller #pylint: disable=C0413

CLIENT = cogo.controller.assign_client()
TOKEN = sys.argv[1]

@CLIENT.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == CLIENT.user:
        return

    if message.content.startswith(''):
        msg = 'Hello {0.author.mention}'.format(message)
        await CLIENT.send_message(message.channel, msg)

@CLIENT.event
async def on_typing(channel, person, when):
    print(channel)
    print(person)
    print(when)

    #msg = 'Hello {user.mention}, I C U typing :eyes:'.format()
    #await CLIENT.send_message(message.channel, msg)

CLIENT.run(TOKEN)

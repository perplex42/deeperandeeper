

from adventuretutorial.game import check_for_save
import pathlib as Path
import adventuretutorial
from typing import Union
import time

import sema
import anyio
import time
from semaphore import Bot, ChatContext


# Connect the bot to number.
bot = Bot("+491711420688")

def respond(ctx: ChatContext):

    return check_for_save(ctx.message.source.number, ctx.message.get_body())


@bot.handler('')
async def echo(ctx: ChatContext) -> None:
    await ctx.message.reply(respond(ctx))

async def main():

    async with bot:

        #await bot.send_message("+4917699811033", "Hi Alex kam das an?")
        #await bot.send_message("+4915144643840", "Hi Ben Kam das an?")

        # Set profile name.
        await bot.set_profile("TROLOLO")

        # Run the bot until you press Ctrl-C.
        await bot.start()


anyio.run(main)

import anyio
import json
import time
from pathlib import Path

import semaphore
from semaphore import Bot, ChatContext

# Connect the bot to number.
bot = Bot("+4915792347840")


@bot.handler('')
async def echo(ctx: ChatContext) -> None:
    playerjson = './player/' + ctx.message.source.number + '.json'

    try:
        with open(playerjson, 'r') as fp:
            player = json.load(fp)
    except FileNotFoundError:
        player = {'number': ctx.message.source.number, 'node': 'start', 'inventory': ['alive']}
        with open(playerjson, 'w') as fp:
            json.dump(player, fp, sort_keys=True, indent=4)

    if ctx.message.get_body() == "reset":
        player = {'number': ctx.message.source.number, 'node': 'start', 'inventory': ['alive']}
        with open(playerjson, 'w') as fp:
            json.dump(player, fp, sort_keys=True, indent=4)
        await ctx.message.reply("Phew - I just restarted ... strange")

    if ctx.message.get_body() == "start":
        time.sleep(5)
        await ctx.message.reply("Hi, äh. moment")
        time.sleep(10)
        await ctx.message.reply("Sekunde ich such grad noch was...")
        time.sleep(10)
        await ctx.message.reply("Bin sofort da. arggg...habs gleich und mach ein Foto!")
        time.sleep(5)
        await ctx.message.reply("so, sorry... ein chaos hier...hier. schreib pic")
        '''
        if ctx.message.get_body() == "pic":
            path = Path(__file__).parent.absolute() / "apod.jpg"
            attachment = {"filename": str(path),
                          "width": "100",
                          "height": "100"}
            print(attachment)
    
            await ctx.message.reply(body="Irgend ne idee was das ist?", attachments=[attachment])
        '''
    elif ctx.message.get_body() == "test":
        player['node'] = 'pinged'
        with open(playerjson, 'w') as fp:
            json.dump(player, fp, sort_keys=True, indent=4)
        await ctx.message.reply("Pong")

    elif ctx.message.get_body() == "ping":
        await ctx.message.reply("Pong")

    else:
        await ctx.message.reply("INVENTORY:"+str(player['inventory']))


async def main():
    async with bot:
        # await bot.send_message("+4917699811033", "Hi Alex kam das an?")
        # await bot.send_message("+4915144643840", "Hi Ben Kam das an?")

        # Set profile name.
        await bot.set_profile("Semaphore example bot")

        # Run the bot until you press Ctrl-C.
        await bot.start()


anyio.run(main)

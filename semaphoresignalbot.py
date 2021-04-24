import anyio
import json
import time
from semaphore import Bot, ChatContext

# Connect the bot to number.
bot = Bot("+4915792347840")

def respond(ctx: ChatContext):
    if ctx.message.get_body() == "start":
        data = {}
        data['player'] = []
        data['player'].append({
            'number': ctx.message.source.number,
            'node': 'start',
            'inventory': ''
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        bot.send_message(ctx.message.source.number, "Sekunde ich such grad noch was...")
        time.sleep(5)
        return "so, sorry... ein chaos hier...los gehts. schreib ping"

    if ctx.message.get_body() == "ping":
        return "Pong"
    return "blablabla"


@bot.handler('')
async def echo(ctx: ChatContext) -> None:
    # wenn nicht existent initplayerjson()
    with open('player.json') as json_file:
        data = json.load(json_file)
    if ctx.message.get_body() == "start":
        data['player'].append({
            'number': ctx.message.source.number,
            'node': 'start',
            'inventory': ''
        })
        with open('player.json', 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(5)
        await ctx.message.reply("Hi, äh. moment")
        time.sleep(10)
        await ctx.message.reply("Sekunde ich such grad noch was...")
        time.sleep(10)
        await ctx.message.reply("Bin sofort da. arggg...habs gleich und mach ein Foto!")
        time.sleep(5)
        await ctx.message.reply("so, sorry... ein chaos hier...hier. schreib pic")


    elif ctx.message.get_body() == "pic":
        path = "/var/www/ludumdare/deeperandeeper/bild.png"
        attachment = {"filename": str(path),
                      "width": "100",
                      "height": "100"}
        print(attachment)
        await ctx.message.reply("Irgend ne idee was das ist?", attachments[attachment])
    elif ctx.message.get_body() == "ping":
        data['player'].append({
            'number': ctx.message.source.number,
            'node': 'start',
            'inventory': 'pinged'
        })
        with open('player.json', 'w') as outfile:
            json.dump(data, outfile)
        await ctx.message.reply("Pong")
    else:
        await ctx.message.reply("blablabla")


async def main():

    async with bot:
        # await bot.send_message("+4917699811033", "Hi Alex kam das an?")
        # await bot.send_message("+4915144643840", "Hi Ben Kam das an?")

        # Set profile name.
        await bot.set_profile("Semaphore example bot")

        # Run the bot until you press Ctrl-C.
        await bot.start()

def initplayerjson():
    data = {}
    data['player'] = []
    with open('player.json', 'w') as outfile:
        json.dump(data, outfile)



anyio.run(main)
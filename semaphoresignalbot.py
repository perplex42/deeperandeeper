import anyio
from semaphore import Bot, ChatContext

# Connect the bot to number.
bot = Bot("+4915792347840")

def respond(ctx: ChatContext):
    if ctx.message.get_body() == "hi":
        return "deine nummer ist"+str(ctx.message.source.number)
        print("number:{}".format(ctx.message.source.number))
    if ctx.message.get_body() == "ping":
        return "Pong"
    return "blablabla"


@bot.handler('')
async def echo(ctx: ChatContext) -> None:
    await ctx.message.reply(respond(ctx))

async def main():

    async with bot:
        # await bot.send_message("+4917699811033", "Hi Alex kam das an?")
        # await bot.send_message("+4915144643840", "Hi Ben Kam das an?")

        # Set profile name.
        await bot.set_profile("Semaphore example bot")

        # Run the bot until you press Ctrl-C.
        await bot.start()





anyio.run(main)
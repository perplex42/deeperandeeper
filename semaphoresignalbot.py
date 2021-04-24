import anyio
from semaphore import Bot, ChatContext

# Connect the bot to number.
bot = Bot("+4915792347840")

def respond(ctx: ChatContext):
    if ctx.message.get_body() == "Hallo":
        return "Selber Hallo"
    if ctx.message.get_body() == "ping":
        return "Pong"
    return ctx.message.


@bot.handler('')
async def echo(ctx: ChatContext) -> None:
    await ctx.message.reply(respond(ctx))

async def main():
    async with bot:
        # Set profile name.
        await bot.set_profile("Semaphore example bot")

        # Run the bot until you press Ctrl-C.
        await bot.start()

anyio.run(main)
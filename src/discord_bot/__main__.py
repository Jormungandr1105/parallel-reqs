import os
from discord.ext import commands
from dotenv import load_dotenv
import subprocess
from job_manager.api import API


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN == "":
	print("NO TOKEN: SET DISCORD_TOKEN IN .ENV TO THE TOKEN FOR YOUR BOT AND TRY AGAIN.")
	exit(1)


Api = API()

bot = commands.Bot(command_prefix='dt')

@bot.event
async def on_ready():
	print("{0} spinning up".format(bot.user.name))

@bot.command(name="queue")
async def dtqueue(ctx,*,arg=None):
	if arg == None:
		arg = "basic"
	response = Api.show_queue(arg)
	response = """```bash\n{0}```""".format(response)
	await ctx.send(response)

@bot.command(name="run")
async def run(ctx,*,arg=None):
	response = "This command is currently under construction\nTry again later, or get off your ass and finish it."
	await ctx.send(response)


bot.run(DISCORD_TOKEN)
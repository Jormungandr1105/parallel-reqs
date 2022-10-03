import os
import discord
from dotenv import load_dotenv
import subprocess
from job_manager.api import API


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN == "":
	print("NO TOKEN: SET DISCORD_TOKEN IN .ENV TO THE TOKEN FOR YOUR BOT AND TRY AGAIN.")
	exit(1)


Api = API()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	print("{0} spinning up".format(bot.user.name))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.startswith('dt'):
		msg = message.content[2:]
		args=msg.split(" ")[1:]
		print(args)
		if msg[:5] == "queue":
			await dtqueue(args,message.channel)
		elif msg[:3] == "run":
			await dtrun(args,message.channel)

async def dtqueue(args,ctx):
	if args == []:
		args = "basic"
	else:
		args = args[0]
	response = Api.show_queue(args)
	response = """```bash\n{0}```""".format(response)
	await ctx.send(response)

async def dtrun(args,ctx):
	response = "This command is currently under construction\nTry again later, or get off your ass and finish it."
	await ctx.send(response)


bot.run(DISCORD_TOKEN)
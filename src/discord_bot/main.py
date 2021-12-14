import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv

def boot():
	load_dotenv()
	DISCORD_TOKEN = os.getenv("discord_token")


def run():
	pass

if __name__ == '__main__':
	boot()
	run()
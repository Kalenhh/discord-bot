#!/usr/bin/python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "*", description = "lol")

@bot.event
async def on_ready():
	print("Ready !")

@bot.command()
async def EDT(ctx):
	await ctx.send("https://cdn.discordapp.com/attachments/750374328398249985/779049032802762834/unknown.png")

@bot.command()
async def ryan(ctx):
	await ctx.send("miskin boloss")

bot.run("Nzc3OTcwMzg3NDEyNTgyNDEw.X7LLYg.98wsHtneuBWUgEtmr43MXqol5-U")



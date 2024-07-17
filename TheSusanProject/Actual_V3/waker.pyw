import ctypes
import time
import json

def prevent_system_sleep(display_on=False):
	ES_CONTINUOUS = 0x80000000
	ES_SYSTEM_REQUIRED = 0x00000001
	ES_DISPLAY_REQUIRED = 0x00000002

	flags = ES_CONTINUOUS | ES_SYSTEM_REQUIRED
	if display_on:
		flags |= ES_DISPLAY_REQUIRED

	result = ctypes.windll.kernel32.SetThreadExecutionState(flags)
	
	if result == 0:
		raise RuntimeError("Failed to set thread execution state")

def allow_system_sleep():
	ES_CONTINUOUS = 0x80000000

	result = ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
	
	if result == 0:
		raise RuntimeError("Failed to reset thread execution state")

try:
	with open("relax.json", "r") as f:
		sData = json.loads(f.read())
		oristate = sData["sleepmode"]
except (FileNotFoundError, KeyError):
	with open("relax.json", "w") as f:
		f.write(json.dumps({"time": 5, "sleepmode": [True, False]}, indent=4))
		oristate=[True, False]

# [SleepDeprived, DisplayOn]

try:
	while True:
		with open("relax.json", "r") as f:
			sData = json.loads(f.read())
			state = sData["sleepmode"]
		if state==oristate:
			pass
		else:
			if state[0]:
				prevent_system_sleep(display_on=state[1])
			else:
				allow_system_sleep()
			oristate=state
except:
	allow_system_sleep()
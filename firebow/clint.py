# Clint.py

import firebase_admin
from firebase_admin import credentials, db
import os

uname=input("Uname: ")
if not uname:
	uname=os.environ["username"]
cred = credentials.Certificate('tempest.json')
firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://mysamplecodetest-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def send_command(command):
	ref = db.reference(f'/{uname}/commands') 
	ref.push(command)
	print(f"Sent command: {command}")

if __name__ == '__main__':
	while True:
		command = input(f"\n{uname}:Cmd> ")
		if not command:
			uname=input("Uname: ")
			if not uname:
				uname=os.environ["username"]
		elif command==".clear":
			db.reference(f'/{uname}/commands').delete()
			print("Commands Cleared")
		else:
			send_command(command)

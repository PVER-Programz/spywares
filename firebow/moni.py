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

def listen_for_feedbacks():
	ref = db.reference(f'/{uname}/feedback') 

	while True:
		feed_data = ref.get()  # Get all commands
		if feed_data:
			for key, command in feed_data.items():
				print()
				print(command)
				ref.child(key).delete()  


if __name__ == '__main__':
	listen_for_feedbacks()
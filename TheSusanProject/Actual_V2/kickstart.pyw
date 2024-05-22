import os

filepath = ["c:/systems/sdb.pyw", "c:/systems/rc.pyw"]

os.chdir("c:/systems")

for file in filepath:
	os.startfile(file)

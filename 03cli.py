# Command Line interface 
# This python script sends GET request to localhost:8080 to 
# get the JSON and then processes it
import time
import json
import requests
URL = "http://localhost:8080"
BusNo = input("Enter Bus Number - 21, 34, 16, 3, 17, 13, 18, 36, 24, 14, 4, 6, 1, 35, 9, 23, 22, 20, 19, 11, 15, 2 : ")
lat = ""
lon = ""
speed = ""
loc = ""
state = ""

print("Latitude\t\tLongitude\t\tSpeed\t\tState\t\tLocation\n")
while True:
	r = requests.get(URL) # GET Request
	data = r.json()
	for x in data["busDetails"]:
		if x["busNum"] == BusNo:
			lat = x["lat"][0:5]
			lon = x["lng"][0:5]
			speed = x["speed"][0:5]
			loc = x["location"]
			if x["isMoving"] == "1":
				state = "Moving"
			else: 
				state = "Stopped"
			break
	print(lat+"\t\t"+lon+"\t\t"+speed+"\t\t"+state+"\t\t"+loc+"\n")
	time.sleep(3)





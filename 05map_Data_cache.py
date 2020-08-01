# This python script was used to perform Reverse Geolocation on a grid of coordinates to and then store/cache their data in a text file
# The reverse geolocation was CACHED done using the Open Street Maps API

import json
import requests

a = 19.36 # Latitude Initial
b = 19.15 # Latitude Final

c = 84.70 # Longitude Initial
d = 85.01 # Longitude Final
lat = str(a)
lon = ""
file = open('0MpCachFn4.txt', 'w')
while a > b:
	lat = str(a)
	while c < d:
		lon = str(c)
		URL = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + lat + "&lon=" + lon # Open Street Maps API
		res = requests.get(URL)	
		cont = res.json()
		file.write(lat + "\n")
		file.write(lon + "\n")
		file.write(cont["display_name"] + "\n")
		c = c + 0.01
		print(lat + " " + lon + " " + cont["display_name"] + "\n")
	c = 84.70
	a = a - 0.01

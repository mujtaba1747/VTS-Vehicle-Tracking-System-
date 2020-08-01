# This Python code randomizes all the JSONs I collected because they all were same
# I randomized the Latitude, Longitude, Speed and Used the Cached Map data to add Location of each bus to the JSON 
import json
import random
Map = {}# Map to store the Address of each point in grid Latitude 19.15 to 19.37 and Longitude 84.70 to 85.00
for i in range(1914, 1937):       # Initializing the Key and Nested Key with Value (Empty String)
	Map[i] = {}
	for j in range(8470, 8501):
		Map[i][j] = ""

# List to read the Map Cache Line by Line
FileList = [] 
FileList = [line.rstrip('\n') for line in open("0MapCache.txt")] # Reading the Map Cache line by line and storing in a List Temporarily

# Initializing Dictionary
for z in range(0, len(FileList), 3):            
	lat = ((int)(((float)(FileList[z]))*100))         # Converted all Latitude Float to int ans multiplied to store properly in Dictionary
	lon = ((int)(((float)(FileList[z + 1]))*100))	  # This was done to avoid Floating Point Imprecision from creeping into the Dictionary
	loc = FileList[z + 2] 
	Map[lat][lon] = loc  # Finally Storing in the Nested Dictionary
x = 19.3600000000 # Initial Latitude
y = 84.7000000000 # Initial Longitude

# Storing all possible Longitudes in one List and all Latitudes in another as they will be required in randomizing the location in the JSONs
latitude = []
longitude = []
while x >= 19.15:
    latitude.append((int)(x*100)) 
    x = x - 0.01
while y <= 85.00:
    longitude.append((int)(y*100))
    y = y + 0.01
#-----------------------------------------------------------------------------------------------------#
#Randomizing all 1547 JSONs I scraped
counter = 0
while counter <= 1547:
	file = "json" + str(counter) + ".json"
	with open(file) as f:
		data = json.load(f)
	for Eachbus in data["busDetails"]:
		Eachbus["lat"] = str((random.choice(latitude)/100.00))
		Eachbus["lng"] = str((random.choice(longitude)/100.00))
		Eachbus["speed"] = str((random.randrange(100, 1000)/11.00))
		Eachbus["location"] = Map[(int)(((float)(Eachbus["lat"]))*100)][(int)(((float)(Eachbus["lng"]))*100)] 
		if Eachbus["speed"] == "0":
			Eachbus["isMoving"] = "0"
		else:
			Eachbus["isMoving"] = "1"
	file_obj = open(file, 'w')       ## Overwriting the identical JSONs with Randomized JSONs
	json.dump(data, file_obj)        
	counter = counter + 1
#-----------------------------------------------------------------------------------------------------#


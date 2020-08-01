##Written below is the Python Code used to get the JSON from the server
##It will be used to cache the bus data
##Reference : https://stackoverflow.com/questions/57980528/what-is-the-meaning-of-rand-in-the-url-phpl-domain-namep-smartdomain-name
import requests
import json
import time
from random import randint

f = open("TimeLog.txt", 'a')
n = 16   
for x in range(5000):  
	start = time.time()           
	cache_buster = ''.join(["%s" % randint(0, 9) for num in range(0, n)])    ## Used to avoid getting a cached copy from the server 
	URL = "http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist&rand=0." + cache_buster
	res = requests.get(URL)													 																							 
	cont = res.json()
	s = 'json' + str(x) + '.json'	  																							
	with open(s, 'w') as json_file:  								
		json.dump(cont, json_file)
	elapsed = time.time() - start
	if elapsed < 5:
		time.sleep(5 - elapsed)  # Collecting Every 5 seconds
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print(current_time)
	f.write(current_time + "\n")
	##m = json.dumps(z)
f.close()


